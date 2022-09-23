from distutils.debug import DEBUG
from dotenv import load_dotenv, find_dotenv
from os import environ


dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=False)

AWS_ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = environ.get('AWS_BUCKET_NAME')
AWS_PROJECT_NAME = environ.get('AWS_PROJECT_NAME')
AWS_REGION = environ.get('AWS_REGION')
AWS_BUCKET_ENDPOINT = environ.get('AWS_BUCKET_ENDPOINT')

class ConfigDev:
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    JWT_SECRET_KEY = environ.getenv("JWT_SECRET_KEY")

class ConfigProd:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
