from app.file.models import File
from app.file.schemas import FileSchema
from app.services import BaseCRUDServices


class FileServices(BaseCRUDServices[File, FileSchema]):
    pass


file_services = FileServices(File)