from app.auth.controller import Login
from flask import Blueprint

auth_api = Blueprint('auth_api', __name__)



auth_api.add_url_rule('/login', view_func = Login.as_view('user_login'), methods = ['POST'])