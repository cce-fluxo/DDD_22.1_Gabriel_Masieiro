from app.model import BaseModel
from app.administrador.model import Administrador
from app.usuario_comum.model import UsuarioComum
from app.extensions import db
import bcrypt 
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from datetime import timedelta, datetime

class User(BaseModel):
    
    # Toda tabela deve possuir um nome, deve ser em letrta minúscula a sua inicial
    __tablename__ = 'user'

    # Os modelos, atributos pertencentes a esta tabela
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idade = db.Column(db.Integer, nullable = False)
    nome = db.Column(db.String(80), nullable = False)
    sobrenome = db.Column(db.String(100), nullable = False)
    cpf = db.Column(db.String(15), nullable = False, unique = True)
    email = db.Column(db.String(70), nullable = False, unique = True, index = True)
    senha_hash = db.Column(db.LargeBinary(128))
    verificationPinHash = db.Column(db.LargeBinary(128))
    createdPinTimestamp = db.Column(db.DateTime) 
    role_user = db.Column(db.String(20))

    #One-to-many Relationships
    administrador = db.relationship('Administrador', back_populates = 'user', uselist = False)
    usuario_comum = db.relationship('UsuarioComum', back_populates = 'user', uselist = False)


    # Abaixo será implementado o código para especificar o usuário que está logando
    # User Password
    @property
    def role(self):

        return self.role_user

    @role.setter
    def role(self, role):
        # Colocar os usuarios que estou relacionando
        if role.lower() in ('usuario_comum', 'administrador'):
            self.role_user = role.lower()

        else:
            raise KeyError('User role not specified')
    
    def role_specify(self):

        if self.role_user == 'usuario_comum':
            user_specified = UsuarioComum(user_id = self.id)
            user_specified.save()

        else:
            user_specified = Administrador(user_id = self.id)
            user_specified.save()
    

    @property
    def senha(self):

        raise AttributeError('Password is not a readable attribute')

    # Decorator para o tratamento da senha
    @senha.setter
    def senha(self, senha) -> None:

        # A senha vem como string e é transformada em binário a partir do .encode
        # A senha como binário possui o hash e sobre esta é adicionado o salt
        self.senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

    def verify_password(self, senha) -> bool:

        return bcrypt.checkpw(senha.encode(), self.senha_hash)
    
    def token(self) -> str:

        return create_access_token(
            identity = self.id,
            expires_delta = timedelta(minutes=1440),
            fresh = True,
            additional_claims={"role_user":self.role_user})
    
    def refresh_token(self) -> str:

        return create_refresh_token(
            identity = self.id,
            expires_delta = timedelta(minutes=2880))
    
    @staticmethod
    def verify_token(token) -> object:

        try:
            data = decode_token(token)

        except:
            return None
        
        user = User.query.get(data['identity'])

        return user

    @property
    def verificationPin(self):
        raise AttributeError('verification pin is not a readable attribute.')
        
    @verificationPin.setter
    def verificationPin(self, verificationPin):
        self.createdPinTimestamp = datetime.now()
        self.verificationPinHash = bcrypt.hashpw(verificationPin.encode(), bcrypt.gensalt())
    
    def verify_pin(self, verificationPinReceived):
        timeDifference = round((datetime.now() - self.createdPinTimestamp).seconds / 60)
        return bcrypt.checkpw(verificationPinReceived.encode(), self.verificationPinHash) and timeDifference <= 5
