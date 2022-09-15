from app.extensions import db
from app.model import BaseModel

class Arquivo(BaseModel):

    __tablename__ = 'arquivo'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # inserir atributos para arquivos

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates = 'arquivo')