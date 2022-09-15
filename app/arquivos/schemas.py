#from json import load
from ..extensions import ma
from .model import Arquivo

class ArquivoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Arquivo
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
