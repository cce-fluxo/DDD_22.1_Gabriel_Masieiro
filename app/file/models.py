from app.model import BaseModel
from app.extensions import db
from app.association import associationAuthorFile, associationTagFile
from datetime import datetime

class File(BaseModel):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creationTimeStamp = db.Column(db.DateTime, default=datetime.now())
    media_path = db.Column(db.String(300))
    type = db.Column(db.String(100))
    click_quantity = db.Column(db.Integer)
    title = db.Column(db.String(100))
    category = db.Column(db.String(100))
    area = db.Column(db.String(100))
    year = db.Column(db.Integer)
    awarded = db.Column(db.String(100))
    description = db.Column(db.String(100))

    authors_associated = db.relationship("Author", secondary=associationAuthorFile, backref='files')
    tags_associated = db.relationship("Tag", secondary=associationTagFile, backref='files')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))