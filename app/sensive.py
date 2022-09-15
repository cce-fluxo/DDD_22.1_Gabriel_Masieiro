# guardar arq sensíveis do usuario
class Sensive:
    # onde está o banco de dados

    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    JSON_SORT_KEYS = False
    #Chave
    JWT_SECRET_KEY = "ERQTYUIODFGHJKCVBNMFFDHJSKYDEIQWSOKEDUQJWI"
    # aplicação do sendgrid
    # aplicação sendgrid, pode ser uma possível fonte de erros, 
    # não consegui utilizar a plataforma por falta de autorização por parte da mesma
    # assim não consegui pegar alguns atributos essenciais para o correto funcionamento do código

    MAIL_SERVER = ""
    MAIL_PORT = ""
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = ""
    MAIL_USE_SSL = ""

sen = Sensive()