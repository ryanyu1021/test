# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('I3xsLRgtFFb6EAMTOdb9wmx1VEyGXFnr0OpBxlYgeQLASMAkZBt+OpKOb47yzz3dNGESo0773xyCaJQVJkmB9sJ2QvexdQ2asDHdwLsntWBcF3GYsfC2dEeWvuwOCJOrQS6kHcXV6OvZhI84l7TOPQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f45c84416c2c7760815a5fb747f46517')



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name
    uid = profile.user_id
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=uid))
 

print('juhuhu')

if __name__ == '__main__':
    app.run(debug=True)


for i in range(0,10):
    print(i)