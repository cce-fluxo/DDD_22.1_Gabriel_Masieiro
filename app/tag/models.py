from app.model import BaseModel
from app.extensions import db
from app.association import associationTagFile


# Entidade de tag, a ser associada a um arquivo
class Tag(BaseModel):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)