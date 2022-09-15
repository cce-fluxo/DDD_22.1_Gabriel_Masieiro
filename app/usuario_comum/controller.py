from ..user.model import User
from ..user.schemas import UserSchema
from flask import request, jsonify
from flask.views import MethodView

class UsuarioComumList(MethodView): #/usuario_comum/lista

    def get(self):

        pagina = request.args.get('pag', 1, type=int)

        usuarios_comuns = User.query.filter_by(role_user="Aluno").paginate(page=pagina, per_page=5)

        schema = UserSchema(many=True)

        return jsonify(schema.dump(usuarios_comuns.items)), 200
        