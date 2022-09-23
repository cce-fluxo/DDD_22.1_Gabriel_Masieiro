from app.user.model import User
from app.user.schemas import UserSchema
from app.services import BaseCRUDServices


class UserServices(BaseCRUDServices[User, UserSchema]):
    def get_by_email(self, email: str) -> User:
        return self.model.query.filter_by(email=email).first()

user_services = UserServices(User)