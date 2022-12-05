
# 載入LineBot所需要的套件
import os
import re

from flask import Flask, request, abort
from linebot import (
    LineBotApi, 
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from gs import GoogleSheets

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(
    'r09tEwKEF/Gkp25nPDsYDiFl4xTDFWDhh1tCh9pFWDBpCmi0G5pkpZhp8vKJLNrcV0bKaDYZXilfdv/G2WEAeNSUyVmmeILVd69D3i/XvOrXs7T04z3ARzpmQWaJb+uBL+UT0k38G2m/yzc2qzlgyAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('c68620cabd079b54cb7f24242e06f1c2')

# line_bot_api.push_message(
#     'U24b0637188410e7322658cd63fbe85b9', TextSendMessage(text='你可以開始了'))


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


# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    if re.match('col', message):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(GoogleSheets.columns))
    else:
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(message))


# 主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
