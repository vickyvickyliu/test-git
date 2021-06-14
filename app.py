from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from appnew import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('rJEleCsjWB6K1JbL7GEeuA97VtYBUjaKeav4nH+33ajx5rXuwFxQdjJ0PCqALVQPt3Mk6bZx6giFImad7eMFHEzJYnvB4ELf31UTr2yZ3HpZsHPz9+ppr7M5YtihtVGIFh0WWoSC4lyS0iDDcr3BiAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e5656d0269c4c60d4d149288d67e3083')
mydict={}
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    try:
        line_id=event.source.user_id
        line_bot_api.push_message('Udf7af3efedecd6323e16491c202af7ac',TextSendMessage(text=line_id+'發了:'+msg))
        '''try:
            line_bot_api.multicast(['Udf7af3efedecd6323e16491c202af7ac', 'Ude8b39f4c814be323dba05addd90a40a'], TextSendMessage(text=uu+"發了:"+msg))
        #uu=event.source.user_id
        #line_bot_api.multicast(['Udf7af3efedecd6323e16491c202af7ac', 'U0b7c9d483a2832b52d89e7d6f8820284','','','',''], TextSendMessage(text=uu+"發了:"+msg))
        except:
            message = TextSendMessage(text="錯誤")
            line_bot_api.reply_message(event.reply_token, message)  '''
    except:
        message = TextSendMessage(text="錯誤")
        line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.push_message(uu,TextSendMessage(text=uu+msg))
    if '會員' in msg:
        message = membersystem()
        line_bot_api.reply_message(event.reply_token, message)
    elif '尋找共乘' in msg:
        message = findjustgo()
        line_bot_api.reply_message(event.reply_token, message)
    elif '即時資訊' in msg:
        message = nowinformation()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我要揪車' in msg:
        message =  call()
        line_bot_api.reply_message(event.reply_token, message)
    elif '揪車情況/取消揪車' in msg:
        message = justgosystem()
        line_bot_api.reply_message(event.reply_token, message)
    elif '使用說明/QA/其他' in msg:
        message = others()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊' in msg:
        try:
            if line_id not in mydict:
                mydict[line_id]={}
                mydict[line_id]["register"]={}

                line_bot_api.push_message(line_id,TextSendMessage(text='檢測到此id未註冊過，進行註冊程序'))
            else:
                line_bot_api.push_message(line_id,TextSendMessage(text='檢測到此id註冊過，進行更改資料程序'))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="失敗"))
        #message = keyword()
        #line_bot_api.reply_message(event.reply_token, message)
    #測試用
    elif '呼叫字典' in msg:
        message = str(mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    #洪學姊部分
    elif '_dbmbcheck' in msg: # 註冊的回覆
        message = name()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_name' in msg: # name的回覆
        message = student_id()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_sid' in msg:  # student_id的回覆
        message = depart()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_depart' in msg: # depart的回覆
        message = sex()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_sex' in msg: # sex的回覆
        message = password()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_idpass' in msg: # password的回覆
        message = password_check()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_passchk' in msg: # password_check的回覆
        message = email_check()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    #管理員回訊息
    elif '回訊息' in msg:
        try:
            replayid=msg[:33]
            massage=msg[37:]+"\nby管理員"
            line_bot_api.push_message(replayid,TextSendMessage(text=massage))
        except:
            #line_bot_api.push_message(line_id,TextSendMessage(text="失敗"))
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請點選圖文表單上的功能，進入服務喔！'))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='訊息回覆成功'))
    else:
        message = TextSendMessage(text="請點選圖文表單上的功能，進入服務喔！")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
