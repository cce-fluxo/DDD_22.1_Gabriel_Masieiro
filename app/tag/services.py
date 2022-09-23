from app.tag.models import Tag
from app.tag.schemas import TagSchema
from app.services import BaseCRUDServices


class TagServices(BaseCRUDServices[Tag, TagSchema]):
    pass

tag_services = TagServices(Tag)