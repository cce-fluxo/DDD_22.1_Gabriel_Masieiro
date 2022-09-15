from flask import Flask
from .config import ConfigProd
from .extensions import db, migrate, mail, jwt, ma
from app.user.routes import user_api
from app.auth.routes import auth_api
from app.usuario_comum.routes import usuariocomum_api
from app.administrador.routes import administrador_api
from app.arquivos.routes import arquivo_api
#para o storage
from app.file.routes import file_api
from app.storageDireto.routes import storageDireto_api
from app.storagePreSigned.routes import storagePreSigned_api


# Essa função serve para criar um app, uma aplicação
def create_app():

    app = Flask(__name__, instance_relative_config=True)
    # rever essa linha de cdg abaixo
    #app.config['SECRET_KEY'] = 'Fluxo'

    # quer dizer que o app vai ter as configurações do objeto da classe Config
    app.config.from_object(ConfigProd)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    
    app.register_blueprint(user_api)
    app.register_blueprint(auth_api)
    app.register_blueprint(usuariocomum_api)
    app.register_blueprint(administrador_api)
    app.register_blueprint(arquivo_api)

    # para o storage
    app.register_blueprint(file_api)
    app.register_blueprint(storageDireto_api)
    app.register_blueprint(storagePreSigned_api)



    # estamos retornando a aplicação feita
    return app