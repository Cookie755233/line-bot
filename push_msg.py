from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('你自己的token')
# 請填入您的ID
yourID = '你自己的ID'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='hello world!'))