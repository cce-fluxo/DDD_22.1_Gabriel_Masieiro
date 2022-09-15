from app.extensions import ma
from app.messages.model import Message

class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
    title = ma.String(required=True)
    text = ma.String(required=True)

    writer = ma.Integer(required=True)