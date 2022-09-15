from flask import request
from flask.views import MethodView
from app.messages.model import Message
from app.messages.schema import MessageSchema
from app.utils.filters import filter


class MessageList(MethodView):     # /messages
    def get(self):
        schema = filter.getSchema(qs=request.args, schema_cls=MessageSchema, many=True)
        messages = Message.query.all()
        return schema.dump(messages), 200


    def post(self):
        data = request.json
        schema = MessageSchema()
        message = schema.load(data)
        message.save()
        return schema.dump(message), 201