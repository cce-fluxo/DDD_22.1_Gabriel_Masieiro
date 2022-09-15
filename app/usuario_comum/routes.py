from flask import Blueprint
from .controller import UsuarioComumList

usuariocomum_api = Blueprint('aluno_api', __name__)

usuariocomum_api.add_url_rule('/aluno/lista', view_func = UsuarioComumList.as_view('usuariocomum_list'), methods = ['GET'])
