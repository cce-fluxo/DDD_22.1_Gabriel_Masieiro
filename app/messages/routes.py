from flask import Blueprint
from app.messages.controller import MessageList

message_api = Blueprint('message_api', __name__)

message_api.add_url_rule(
    '/messages',
    view_func=MessageList.as_view('message_list'),
    methods=['GET', 'POST']
)