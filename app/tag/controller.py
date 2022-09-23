from flask import jsonify, request
from flask.views import MethodView
from app.tag.models import Tag
from app.tag.schemas import TagSchema
from app.tag.services import tag_services
from marshmallow.exceptions import ValidationError

# /tag/create
class TagCreate(MethodView):

    """ Cria nova tag """
    def post(self):
        schema = TagSchema()
        try:
            tag = tag_services.create(request.json, schema)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400
            

        return schema.dump(tag), 200



# /tags
class TagAll(MethodView):

    """ Mostra todas tags em ordem """
    def get(self):
        schema = TagSchema(many=True)
        tags = Tag.query.order_by(Tag.name).all()

        return jsonify(schema.dump(tags)), 200



# /tag/<int:tag_id>
class TagDetails(MethodView):

    """ Pega tag especifica """
    def get(self, tag_id):
        schema = TagSchema()
        tag = Tag.query.filter_by(id=tag_id).first_or_404()

        return schema.dump(tag), 200


    ''' Deleta tag '''
    def delete(self, tag_id):
        tag_services.delete_by_id(tag_id)

        return {"msg": "tag has been deleted"}, 200