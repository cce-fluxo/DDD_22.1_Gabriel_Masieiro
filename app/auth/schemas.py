from ..extensions import ma

# Verifica se existe erro no input
class LoginSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True, load_only=True)


# Verifica se existe erro no input
class NewPasswordSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True, load_only=True)
    verificationPin = ma.String(required=True, load_only=True)