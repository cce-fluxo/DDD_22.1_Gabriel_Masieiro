from ..extensions import ma
from ..user.model import User

# Importar caso o user tenha relação com as tabelas, como os arquivos por exemplo
# from ..arquivos.schemas import ArquivosSchema


class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User 
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)

    #atributos do usuário
    idade = ma.Integer(required=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    cpf = ma.String(required=True)
    email = ma.Email(required=True)
    senha = ma.String(load_only=True, required=True)
    role_user = ma.String(required=True)

    usuario_comum = ma.Nested('UsuarioComumSchema')
    administrador = ma.Nested('AdministradorSchema')



class LoginSchema(ma.Schema):

    email = ma.Email(required=True)
    senha = ma.String(load_only=True, required=True)