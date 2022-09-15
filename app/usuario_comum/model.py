from app.extensions import db
from app.model import BaseModel

class UsuarioComum(BaseModel):

    __tablename__ = 'usuario_comum'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idade = db.Column(db.Integer, nullable = False)
    nome = db.Column(db.String(80), nullable = False)
    sobrenome = db.Column(db.String(100), nullable = False)
    cpf = db.Column(db.String(15), nullable = False, unique = True)
    email = db.Column(db.String(70), nullable = False, unique = True, index = True)
    senha_hash = db.Column(db.LargeBinary(128))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates = 'usuario_comum')