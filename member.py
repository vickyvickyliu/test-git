from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import psycopg2 as ps
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from string import Template
from pathlib import Path
import random

# 連線Database
def database_connect():
    #connect heroku postgresql
    conn = ps.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                      user="pauvcxweyckeaf",
                      password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                      database="d5251933te7fta",
                      port="5432")
    return conn


# 先判斷是否註冊過
# 經由button按下傳來的msg(註冊)及line_id，判斷此使用者是否註冊過。
'''
已註冊(True)--->linebot進行更名流程(背後運行依然是註冊流程)
未註冊(False)--->linebot直接進行註冊流程
'''
# read member data from database
def read_from_member(line_id):
    conn = database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT * FROM member WHERE student_id is NOT NULL AND line_id = %s"""
    cursor.execute(sql, (line_id,))
    register_or_not = cursor.fetchall()
    if register_or_not != []:
        # 已註冊
        return True
    else:
        # 未註冊
        return False

    cursor.close()
    conn.close()


# Q:new member check, A:none
# msg == '註冊'
def keyword(msg, line_id):
    db_result = read_from_member(line_id)
    if db_result == True:  # 呼叫更改資料的流程
        txt = '''您好！
您已經是我們的會員，
不需再進行註冊。
那我們就視為資料更新的流程呦！
請輸入：【格式：知道_updtinfo】
'''
    elif db_result == False:
        txt = '''歡迎來到會員註冊系統，
本服務現僅供東吳在學學生使用，
一人限註冊一次，
還請特別注意囉！
以下請務必依照問題後的格式回答！
請輸入：【格式：知道_dbmbcheck】
'''
    return txt


# 開始註冊流程(姓名-->學號-->系級-->性別-->密碼)
# 創建新字典
mydcit = {}

# Q:name, A:dbmbcheck(new member check)
def name(msg, line_id):  # msg-->dbmbcheck的回覆
    txt = "請輸入您的姓名：【格式：姓名_name】"
    return txt

# Q:student_id, A:name
def student_id(msg, line_id):  # msg-->name的回覆
    mydcit[line_id] = {
        'register': {
            'name': msg[:msg.index('_')]
        }
    }
    txt = "請輸入您的學號：【格式：學號_sid】"
    return txt

# Q:depart, A:student_id
def depart(msg, line_id):  # msg-->student_id的回覆
    mydict[line_id] = {
        'register': {
            'student_id': msg[:msg.index('_')]
        }
    }
    txt = "請輸入您的系級：【格式：系級_depart】"
    return txt

# Q:sex, A:depart
def sex(msg, line_id):  # msg-->depart的回覆
    mydict[line_id] = {
        'register': {
            'depart': msg[:msg.index('_')]
        }
    }
    txt = "請輸入您的性別：【格式：性別_sex】"
    return txt


# Q:password, A:sex
def password(msg, line_id):  # msg-->sex的回覆
    mydict[line_id] = {
        'register': {
            'sex': msg[:msg.index('_')]
        }
    }
    txt = "請輸入您的密碼：【格式：密碼_idpass】"
    return txt

# Q:password_check, A:password
def password_check(msg, line_id):  # msg-->password的回覆
    mydict[line_id] = {
        'register': {
            'password': msg[:msg.index('_')]
        }
    }
    regis_member = list(mydcit[line_id]['register'].values())
    regis_member[0], regis_member[1] = regis_member[1], regis_member[0]
    regis_member.insert(1, line_id)
    regis_mb_t = tuple(regis_member)

    # name = d[line_id]['register']['name']
    # student_id = d[line_id]['register']['student_id']
    # depart = d[line_id]['register']['depart']
    # sex = d[line_id]['register']['sex']
    # password = d[line_id]['register']['password']
    # credit_index = 0 = d[line_id]['register']['credit_index']
    # cancel_times = 0 = d[line_id]['register']['cancel_times']

    # global regis_member
    # regis_member = (student_id, line_id, name, depart, sex, password, credit_index, cancel_times)

    txt = f'''
以下是您輸入的資料，請確認是否正確。
--------------------------
您的姓名：{regis_member[2]}
您的學號：{regis_member[0]}
您的系級：{regis_member[3]}
您的生理性別：{regis_member[4]}
您設定的密碼：{regis_member[5]}
--------------------------
【格式：正確或錯誤_passchk】
'''
    return txt, regis_mb_t


# 開始驗證流程

#郵件發送函數
def sendMail(toAccount, name, random_num):
    subject = '東吳大學【揪車Go平臺】郵件驗證碼認證'
    SMTPHost = 'smtp.gmail.com'   # 郵件服務器
    fromAccount = 'justgocarpool@gmail.com'  # 寄件信箱
    fromPasswd = 'hjyffibbosdrpduj'  # 寄件郵件授權碼(不是郵箱登錄密碼)

    #建立郵件
    msg = MIMEMultipart()  # 建立MIMEMultipart物件
    msg['Subject'] = Header(subject, 'utf-8')  # 郵件標題
    msg['From'] = fromAccount  # 寄件者
    msg['To'] = toAccount  # 收件者
#     msg["Accept-Language"]="zh-TW"
#     msg["Accept-Charset"]="ISO-8859-1,utf-8"

    # 郵件正文
    template = Template(Path("email_content.html").read_text(encoding='utf-8'))
    body = template.substitute({"name": name,  # 收件人姓名
                                "random_num": random_num})  # 隨機驗證碼
    msg.attach(MIMEText(body, 'html', 'utf-8'))

    # 附件(圖片)
    xlsxpart = MIMEApplication(
        open('justgo.png', 'rb').read())  # 當前目錄下的附件文件
    xlsxpart.add_header('Content-Disposition',
                        'attachment', filename='justgo.png')
    msg.attach(xlsxpart)

    # 使用smtplib模塊發送郵件
    with smtplib.SMTP(host=SMTPHost, port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(fromAccount, fromPasswd)  # 登入寄件者gmail
            smtp.send_message(msg)  # 寄送郵件
            return True
        except Exception as e:
            return False


def random_num():
    # 隨機驗證碼
    num = []
    for i in range(6):
        i = str(random.randint(0, 9))
        num.append(i)
        random_num = ''.join(num)
    return random_num


