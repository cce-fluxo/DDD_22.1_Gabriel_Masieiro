
from flask import Blueprint
from app.user.controller import UserCreate, UserId, UserList

user_api = Blueprint('user_api', __name__)

user_api.add_url_rule('/user', view_func = UserCreate.as_view('user_geral'), methods = ['POST', 'GET'])

user_api.add_url_rule('/user/<int:id>', view_func = UserId.as_view('user_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

user_api.add_url_rule('/user/lista', view_func = UserList.as_view('user_list'), methods = ['GET'])