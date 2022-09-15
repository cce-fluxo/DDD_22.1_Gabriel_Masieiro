from flask import request
from flask.views import MethodView
from ..user.schemas import LoginSchema, UserSchema
from ..user.services import user_services
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

class Login(MethodView): #/login

    def post(self):

        schema = LoginSchema()
        dados = schema.load(request.json)

        user = user_services.get_by_email(dados['email'])

        if not user or not user.verify_password(dados['senha']):
            return {"Error":"Usuário ou senha inválidos"}

        token = user.token()

        refresh_token = user.refresh_token()

        return {"user": UserSchema().dump(user),
                "token":token,
                "refresh_token":  refresh_token}, 200


class TokenRefresh(MethodView):

    decorators = [jwt_required( refresh=True)]

    def get(self): # /refresh-token

        user_id = get_jwt_identity()
        user = user_services.get_by_id(user_id)

        token = create_access_token(
            identity  = user_id,
            expires_delta = timedelta(minutes=900),
            fresh=False,
            additional_claims={"role_user": self.role_user})
        
        refresh_token = user.refresh_token()

        return {
            'user': UserSchema().dump(user),
            'token': token,
            'refresh_token': refresh_token
        }, 200
