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
#from appnew import *
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
        uu=event.source.user_id
        line_bot_api.push_message('Udf7af3efedecd6323e16491c202af7ac',TextSendMessage(text=uu+'發了:'+msg))
        try:
            #line_bot_api.multicast(['Udf7af3efedecd6323e16491c202af7ac', 'Ude8b39f4c814be323dba05addd90a40a'], TextSendMessage(text=uu+"發了:"+msg))
        #uu=event.source.user_id
        #line_bot_api.multicast(['Udf7af3efedecd6323e16491c202af7ac', 'U0b7c9d483a2832b52d89e7d6f8820284','','','',''], TextSendMessage(text=uu+"發了:"+msg))
        except:
            message = TextSendMessage(text="錯誤")
            line_bot_api.reply_message(event.reply_token, message)  
    except:
        message = TextSendMessage(text="錯誤")
        line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.push_message(uu,TextSendMessage(text=uu+msg))
    if '會員' in msg:
        message = membersystem()
        line_bot_api.reply_message(event.reply_token, message)
    elif '揪車情況/取消揪車' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '即時資訊' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我要揪車' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '尋找共乘' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '使用說明/QA/其他' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text="請點選圖文表單上的功能，進入服務喔！")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#mydict={}