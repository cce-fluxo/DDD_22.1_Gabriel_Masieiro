#from json import load
from ..extensions import ma
from .model import Administrador

class AdministradorSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Administrador 
        load_instance = True
        ordered = True
    
    id = ma.Integer(dump_only=True)