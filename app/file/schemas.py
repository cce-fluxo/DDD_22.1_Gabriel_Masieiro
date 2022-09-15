from app.extensions import ma
from app.file.models import File

class FileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = File
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    media_path = ma.String()
    title = ma.String()