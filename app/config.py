import os
from dotenv import load_dotenv

load_dotenv()

class ConfigDev:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class ConfigProd:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
