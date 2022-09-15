from flask import Blueprint
from .controller import ArquivoList

arquivo_api = Blueprint('arquivo_api', __name__)

arquivo_api.add_url_rule('/arquivo/lista', view_func = ArquivoList.as_view('arquivo_list'), methods = ['GET'])