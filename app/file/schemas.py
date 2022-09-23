from app.extensions import ma
from app.file.models import File
from app.author.schemas import AuthorSchema
from app.tag.schemas import TagSchema

class FileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = File
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    creationTimeStamp = ma.DateTime(required=False)
    media_path = ma.String()
    type = ma.String()
    click_quantity = ma.Integer()
    title = ma.String()
    category = ma.String()
    area = ma.String()
    year = ma.Integer()
    awarded = ma.String()
    description = ma.String()
    creator_id = ma.Integer()
    authors_associated = ma.Nested(AuthorSchema, only=['name','id'], many=True)
    tags_associated = ma.Nested(TagSchema, only=['name','id'], many=True)