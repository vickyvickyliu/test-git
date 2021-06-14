from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def membersystem():
    message = TemplateSendMessage(
        alt_text='會員按鈕',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='會員功能',
                    text='請選擇服務',
                    actions=[
                        PostbackTemplateAction(
                            label='註冊',
                            text='12345'
                        ),
                        PostbackTemplateAction(
                            label='登入',
                            text='登入'
                        ),
                        PostbackTemplateAction(
                            label=' ',
                            text=' '
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='會員功能',
                    text='請選擇服務',
                    actions=[
                        PostbackTemplateAction(
                            label='更改密碼/忘記密碼',
                            data='更改密碼/忘記密碼',
                            text='更改密碼/忘記密碼'
                        ),
                        PostbackTemplateAction(
                            label='查看歷史紀錄',
                            data='查看歷史紀錄',
                            text='查看歷史紀錄'
                        ),
                        PostbackTemplateAction(
                            label='查看信用值',
                            data='查看信用值',
                            text='查看信用值'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)

def cancelcheck():
    message = TemplateSendMessage(
        alt_text='是否確定取消共乘？',
        template=ConfirmTemplate(
            text="是否確定取消共乘？",
            actions=[
                PostbackTemplateAction(
                    label="確定取消",
                    text="確定取消",
                    data="確定取消"
                ),
                PostbackTemplateAction(
                    label="放棄取消",
                    text="放棄取消",
                    data="放棄取消"
                )
            ]
        )
    )
    return message

def chooseleadtype():
    message = TemplateSendMessage(
        alt_text='請選擇發車類別',
        template=ConfirmTemplate(
            text="請選擇發車類別",
            actions=[
                PostbackTemplateAction(
                    label="1.確定要發車(已訂車者)",
                    text="sdjiofvnfdjksfjfl",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.滿員後叫車(等人數湊齊才會訂車)",
                    text="2",
                    data="2"
                )
            ]
        )
    )
    return message

def chooselocation():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                ),
                PostbackTemplateAction(
                    label="4.東吳大學城中校區",
                    text="目的地:東吳大學城中校區",
                    data="4"
                )
            ]
        )
    )
    return message

def checkifontime():
    message = TemplateSendMessage(
        alt_text='請確認是否上車(一分鐘內未按將視為跑單)',
        template=ButtonsTemplate(
            text="請確認是否上車\n(一分鐘內未按將視為跑單)",
            actions=[
                PostbackTemplateAction(
                    label="我已上車",
                    text="我已上車",
                    data="我已上車"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ",
                    data=" "
                )
            ]
        )
    )
    return message 
  
def checknumber():
    message = TemplateSendMessage(
        alt_text='您要加入的共乘是編號xx，請確認',
        template=ConfirmTemplate(
            text="您要加入的共乘是編號xx，請確認",
            actions=[
                PostbackTemplateAction(
                    label="是",
                    text="是",
                    data="是"
                ),
                PostbackTemplateAction(
                    label="否",
                    text="否",
                    data="否"
                )
            ]
        )
    )
    return message

'''    dict{
        "lineid":{
            "我要揪車":{
                "name": "劉語萱","學號":"09170101","揪車種類":"人滿再成團"
            }
        }
    }
def we(uu):
    if dict[][register][]userid
    a=dict[uu][register](name)'''

def findjustgo():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message

def call():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message

def nowinformation():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message

def justgosystem():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message

def others():
    message = TemplateSendMessage(
        alt_text='請選擇目弟弟',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message