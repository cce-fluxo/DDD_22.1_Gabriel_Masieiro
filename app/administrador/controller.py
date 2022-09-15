from ..user.model import User
from ..user.schemas import UserSchema
from flask import request, jsonify
from flask.views import MethodView

class AdministradorList(MethodView): #/administrador/lista

    def get(self):

        pagina = request.args.get('pag', 1, type=int)

        adm = User.query.filter_by(role_user="Administrador").paginate(page=pagina, per_page=5)

        schema = UserSchema(many=True)

        return jsonify(schema.dump(adm.items)), 200