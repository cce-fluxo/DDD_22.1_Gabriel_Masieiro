
from flask import Blueprint
from app.user.controller import UserCreate, UserId, UserList
# saber se a rota para o user_login eh necessária aqui ou só na autenticação
#from app.user.controller import UserLogin


user_api = Blueprint('user_api', __name__)

user_api.add_url_rule('/user', view_func = UserCreate.as_view('user_geral'), methods = ['POST', 'GET'])

user_api.add_url_rule('/user/<int:id>', view_func = UserId.as_view('user_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

#user_api.add_url_rule('/user/<int:id>', view_func = UserLogin.as_view('user_login'), methods = ['POST'])

user_api.add_url_rule('/user/lista', view_func = UserList.as_view('user_list'), methods = ['GET'])