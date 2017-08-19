# encoding: utf-8

import os

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent
)

app = Flask(__name__)


line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))  # Your Channel Access Token
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))  # Your Channel Secret


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
def handle_text_message(event):
    text = event.message.text  # message from user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))  # reply the same message from user


@handler.add(FollowEvent)
def handle_follow(event):
    txt = "登録ありがとう"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=txt))  # reply the same message from user


@handler.add(JoinEvent)
def handle_join(event):
    txt = "登録ありがとう"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=txt))  # reply the same message from user


@handler.add(UnfollowEvent)
def handle_unfollow():
    app.logger.info("Got Unfollow event")


@handler.add(LeaveEvent)
def handle_leave():
    app.logger.info("Got leave event")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])