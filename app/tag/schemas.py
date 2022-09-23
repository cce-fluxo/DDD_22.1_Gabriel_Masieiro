from app.extensions import ma
from app.tag.models import Tag


class TagSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tag
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()