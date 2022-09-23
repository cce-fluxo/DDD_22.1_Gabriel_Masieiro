from app.auth.controller import Login, UserPasswordResetEmail, UserPasswordReset, PinInput
#RefreshToken

from flask import Blueprint

auth_api = Blueprint('auth_api', __name__)

auth_api.add_url_rule('/login', view_func = Login.as_view('user_login'), methods = ['POST'])
auth_api.add_url_rule("/pinInserido", view_func=PinInput.as_view("pinInput"), methods=["POST"])
auth_api.add_url_rule("/esquecisenha", view_func=UserPasswordResetEmail.as_view("passwordResetEmailUser"), methods=["POST"])
auth_api.add_url_rule("/esquecisenha/novasenha/<int:user_id>", view_func=UserPasswordReset.as_view("passwordResetUser"), methods=["PATCH"])
#auth_api.add_url_rule("/refreshToken", view_func=RefreshToken.as_view("refreshToken"), methods=["GET"])