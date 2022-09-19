from app.user.model import User
from flask import  request
#from flask import jsonify
from flask.views import MethodView
from app.utils.filters import filter
#from app.utils.filters import parser

#from flask_mail import Message
#from app.extensions import mail, jwt
#import bcrypt
from ..user.schemas import LoginSchema, UserSchema
from ..user.services import user_services
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token
# from app.permissions import self_client_only, self_vendor_only

# O controller cria um user

class UserCreate(MethodView): #/user

    def post(self):

        schema = UserSchema()
        user = user_services.create(request.json, schema)
        user.role_specify()

        return schema.dump(user), 201


class UserList(MethodView): #/user/lista
   
    def get(self):
        schema = filter.getSchema(qs=request.args, schema_cls=UserSchema, many=True)
        users = User.query.all()
        return schema.dump(users), 200
    
    def post(self):
        data = request.json

        possible_user = User.query.filter_by(username=data['username']).first()
        if possible_user:
            return {'error': 'username already chosen'}

        schema = UserSchema()
        user = schema.load(data)
        user.save()
        return schema.dump(user), 201


class UserId(MethodView): #/user/<int:id>

    decorators = [jwt_required()]
    def get(self, id):
        schema = filter.getSchema(qs=request.args, schema_cls=UserSchema)
        user = User.query.get_or_404(id)
        return schema.dump(user), 200

    def put(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        data = request.json
        schema = UserSchema(exclude=['password'])
        user = schema.load(data, instance=user)
        user.update()
        return schema.dump(user), 200
    
    def patch(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        data = request.json
        schema = UserSchema(exclude=['password'])
        user = schema.load(data, instance=user, partial=True)
        user.update()
        return schema.dump(user), 200
    

    def delete(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        User.delete(user)
        return {}, 204

class UserLogin(MethodView): #/login

    def post(self):

        schema = LoginSchema()
        dados = schema.load(request.json)

        user = user_services.get_by_email(dados['email'])

        if not user or not user.verify_password(dados['senha']):
            return {"Error":"Usuário ou senha inválidos"}

        token = create_access_token(identity = user.id)

        refresh_token = create_refresh_token(identity=user.id)

        return {"user": UserSchema().dump(user),
                "token": token,
                "refresh_token": refresh_token}, 200