from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# instanciando cada objeto

# inicializa o banco de dados
db = SQLAlchemy()
# inicializa migrate
migrate = Migrate()
# inicializa o email
mail = Mail()
# inicizaliza o jwt (serve para encriptar de dados, como senhas, por exemplo)
jwt = JWTManager()
#marshmallow
ma = Marshmallow()