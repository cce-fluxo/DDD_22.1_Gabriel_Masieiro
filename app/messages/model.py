from app.extensions import db
from app.model import BaseModel

class Message(BaseModel):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)

    writer = db.Column(db.Integer, db.ForeignKey('user.id'))