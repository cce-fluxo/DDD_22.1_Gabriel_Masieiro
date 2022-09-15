from flask import Blueprint
from .controller import AdministradorList

administrador_api = Blueprint('administrador_api', __name__)

administrador_api.add_url_rule('/administrador/lista', view_func = AdministradorList.as_view('administrador_list'), methods = ['GET'])