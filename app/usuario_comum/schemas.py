#from json import load
from ..extensions import ma
from .model import UsuarioComum

class UsuarioComumSchema(ma.SQLAlchemySchema):

    class Meta:
        model = UsuarioComum
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)
