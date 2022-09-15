from app.model import BaseModel
from app.extensions import db

class File(BaseModel):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_path = db.Column(db.String(300))
    title = db.Column(db.String(100))

    titulo = db.Column(db.String(80), nullable = False)
    descricao = db.Column(db.String(80), nullable = False)
    upload = db.Column(db.String(80), nullable = False)
    categoria = db.Column(db.String(80), nullable = False)
    area = db.Column(db.String(80), nullable = False)
    ano = db.Column(db.String(80), nullable = False)
    autores = db.Column(db.String(80), nullable = False)
    tags = db.Column(db.String(80), nullable = False)
    premiacao = db.Column(db.String(80), nullable = False)
