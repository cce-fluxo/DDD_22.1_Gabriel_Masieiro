from app.model import BaseModel
from app.extensions import db
from app.association import associationAuthorFile

# Entidade de autor, a ser associada a um arquivo
class Author(BaseModel):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)