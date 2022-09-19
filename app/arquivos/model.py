from app.extensions import db
from app.model import BaseModel

class Arquivo(BaseModel):

    __tablename__ = 'arquivo'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    titulo = db.Column(db.String(80), nullable = False)
    descricao = db.Column(db.String(80), nullable = False)
    upload = db.Column(db.String(80), nullable = False)
    categoria = db.Column(db.String(80), nullable = False)
    area = db.Column(db.String(80), nullable = False)
    ano = db.Column(db.String(80), nullable = False)
    autores = db.Column(db.String(80), nullable = False)
    tags = db.Column(db.String(80), nullable = False)
    premiacao = db.Column(db.String(80), nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates = 'arquivo')