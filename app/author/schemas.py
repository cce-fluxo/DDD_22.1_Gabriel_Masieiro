from app.extensions import ma
from app.author.models import Author


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()