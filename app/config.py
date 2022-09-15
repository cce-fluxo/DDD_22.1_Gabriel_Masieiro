import os
from dotenv import load_dotenv

load_dotenv()

class ConfigDev:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class ConfigProd:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
#from app.sensive import sen
'''from os import environ
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=False)
AWS_ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = environ.get('AWS_BUCKET_NAME')
AWS_PROJECT_NAME = environ.get('AWS_PROJECT_NAME')
AWS_REGION = environ.get('AWS_REGION')
AWS_BUCKET_ENDPOINT = environ.get('AWS_BUCKET_ENDPOINT')

class Config:
    # onde está o banco de dados
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False

    # aplicação sendgrid, pode ser uma possível fonte de erros, 
    # não consegui utilizar a plataforma por falta de autorização por parte da mesma
    # assim não consegui pegar alguns atributos essenciais para o correto funcionamento do código

    JWT_SECRET_KEY = "ERQTYUIODFGHJKCVBNMFFDHJSKYDEIQWSOKEDUQJWI"

    # aplicações send
    MAIL_SERVER = sen.MAIL_SERVER
    MAIL_PORT = sen.MAIL_PORT
    MAIL_USERNAME = sen.MAIL_USERNAME
    MAIL_PASSWORD = sen.MAIL_PASSWORD
    MAIL_USE_TLS = sen.MAIL_USE_TLS
    MAIL_USE_SSL = sen.MAIL_USE_SSL'''