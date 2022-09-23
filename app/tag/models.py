from app.model import BaseModel
from app.extensions import db

# Entidade de tag, a ser associada a um arquivo
class Tag(BaseModel):
    __tablename__ = "tag"
    __table_args__= {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)