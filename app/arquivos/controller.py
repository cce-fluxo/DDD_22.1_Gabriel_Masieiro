from warnings import filters
from app.arquivos.model import Arquivo
from ..user.model import User
from ..user.schemas import UserSchema
from flask import request, jsonify, make_response, abort
from flask.views import MethodView
from app.arquivos.schemas import ArquivoSchema
from app.utils.filters import filter
#from app.utils.filters import parser

#from app.service.model import Service


class ArquivoList(MethodView): #/arquivo/lista

    def get(self):

        pagina = request.args.get('pag', 1, type=int)

        arquivos = User.query.filter_by(role_user="Arquivo").paginate(page=pagina, per_page=5)

        schema = UserSchema(many=True)

        return jsonify(schema.dump(arquivos.items)), 200

    # Rever essa função debaixo
    def ArquivoDetails(MethodView):

        def get(self, arquivo_id):

            arquivo = Arquivo.query.get_or_404(arquivo_id)
            schema = filter.getSchema(qs=request.args, schema_cls=ArquivoSchema)

            return schema.dump(arquivo), 200