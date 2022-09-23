from app.author.models import Author
from app.author.schemas import AuthorSchema
from app.services import BaseCRUDServices


class AuthorServices(BaseCRUDServices[Author, AuthorSchema]):
    pass

author_services = AuthorServices(Author)