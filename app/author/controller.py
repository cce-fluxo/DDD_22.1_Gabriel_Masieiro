from flask import jsonify, request
from flask.views import MethodView
from app.author.models import Author
from app.author.schemas import AuthorSchema
from app.author.services import author_services
from marshmallow.exceptions import ValidationError 

# /autor/create
class AuthorCreate(MethodView):

    """ Cria novo(a) autor """
    def post(self):
        schema = AuthorSchema()
        try:
            author = author_services.create(request.json, schema)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        return schema.dump(author), 200

# /autores
class AuthorsAll(MethodView):

    """ Mostra todos autores em ordem """
    def get(self):
        schema = AuthorSchema(many=True)
        authors = Author.query.order_by(Author.name).all()

        return jsonify(schema.dump(authors)), 200



# /autor/<int:author_id>
class AuthorDetails(MethodView):

    """ Pega autor especifico """
    def get(self, author_id):
        schema = AuthorSchema()
        author = Author.query.filter_by(id=author_id).first_or_404()

        return schema.dump(author), 200


    ''' Deleta autor '''
    def delete(self, author_id):
        author_services.delete_by_id(author_id)

        return {"msg": "author has been deleted"}, 200