from flask import request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from random import randint
from app.user.model import User

from ..user.schemas import LoginSchema, UserSchema
from ..user.services import user_services
from ..user.model import User
from ..auth.schemas import NewPasswordSchema

from marshmallow.exceptions import ValidationError

class Login(MethodView): #/login

    def post(self):

        schema = LoginSchema()
        data = schema.load(request.json)
        user = user_services.get_by_email(data['email'])

        if not user or not user.verify_password(data['senha']):
            return {"Error":"Usuário ou senha inválidos"}, 400

        if user.isAdmin == True:
            access_token = create_access_token(identity=user.id, additional_claims={"isAdmin":True})           
        elif user.isAdmin == False:
            access_token = create_access_token(identity=user.id, additional_claims={"isAdmin":False})
                
        token = user.token()
        refresh_token = user.refresh_token()

        return {"user": UserSchema().dump(user),
                "acess_token": access_token,
                "refresh_token": refresh_token,
                "token":token,
                "isAdm": user.isAdmin,
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
            'refresh_token': refresh_token}, 200

class UserPasswordResetEmail(MethodView):

    """ Envia email com pin de trocar de senha """
    def post(self):

        schema = LoginSchema(exclude=['password'])

        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404()

        verificationPin = str(randint(100000, 999999))
        user.verificationPin = verificationPin
        user.save()
        return {"msg": "email enviado com pin",
                "verificationPin": verificationPin,
        }, 200

class PinInput(MethodView):

    """ Recebe pin do usuario e verifica se é valido """
    def post(self):

        schema = NewPasswordSchema(exclude=['password'])

        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404({"msg": "email não encontrado"})

        if not user or not user.verify_pin(data['verificationPin']):
            return {"code_status": "invalid user or pin"}, 401

        return {"isPinValid": True}, 200


# /esquecisenha/novasenha/<int:user_id>
class UserPasswordReset(MethodView):

    """ Usuario trocar de senha com pin """
    def patch(self):

        schema = NewPasswordSchema()
        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404()

        if not user or not user.verify_pin(data['verificationPin']):
            return {"code_status": "Invalid user or pin"}, 401
        
        user.createdPinTimestamp += timedelta(minutes=5)
        user.password = data['password']
        user.save()

        return {"msg": "Password has been successfully reset"}, 200