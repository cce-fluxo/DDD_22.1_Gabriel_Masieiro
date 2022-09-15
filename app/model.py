from .extensions import db

class BaseModel(db.Model):
    # Classe abstrata, isto é, a classe BaseModel não é um objeto, é uma classe abstrata
    __abstract__ = True 

    # Funções que serão passadas para as tabelas, isto é, para as classes que modelam 
    # as tabelas correspondentes.

    @classmethod
    def create(cls, **data) -> object:
        return cls(**data)
    
    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.save(self)
        db.session.commit()

    def update(self):
        db.session.commit()