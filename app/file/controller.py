from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from app.file.models import File
from app.file.schemas import FileSchema
from app.extensions import db
from sqlalchemy import exc

#/file
class FileAll(MethodView):
    
    # Faz o cadastro de um novo arquivo no banco de dados
    def post(self):
        schema = FileSchema()
        arquivo = schema.load(request.json)
        db.session.add(arquivo)

        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))

        return schema.dump(arquivo), 201

    ''' Pega todos arquivos do banco de dados '''
    def get(self):
        schema = FileSchema(many = True)
        return jsonify(schema.dump(File.query.all())),200

# /file/<int:id>
class FileDetails(MethodView):

    ''' Altera dados de arquivo especifico '''
    def patch(self, id):
        file = File.query.get_or_404(id)
        schema = FileSchema()
        file = schema.load(request.json, instance=file, partial = True)

        db.session.add(file)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(file),200
    
    
    ''' Pega arquivo especifico '''
    def get(self, id):
        schema = FileSchema()
        file = File.query.filter_by(id=id).first_or_404()

        return schema.dump(file), 200

    ''' Deleta arquivo '''
    def delete(self, id):
        file = File.query.get_or_404(id)
        db.session.delete(file)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))
        return {"msg":"Arquivo deletado!"},200