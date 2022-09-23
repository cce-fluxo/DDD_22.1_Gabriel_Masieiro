from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from app.file.models import File
from app.file.schemas import FileSchema
from app.extensions import db
from sqlalchemy import exc
from app.author.models import Author
from app.tag.models import Tag
from app.user.model import User
import json

#/file
class FileAll(MethodView):
    
    # Faz o cadastro de um novo arquivo no banco de dados
    def post(self):
        schema = FileSchema()

        data = request.json

        author_id = data.pop('author', None)
        creator_id = data.pop('creator', None)
        tag_id = data.pop('tag', None)
        
        acervo = schema.load(data)
        
        # Association
        for id in author_id:
            author = Author.query.get(id)
            acervo.authors_associated.append(author)

        for id in tag_id:
            tag = Tag.query.get(id)
            acervo.tags_associated.append(tag)

        creator = User.query.get(creator_id)
        acervo.creator_id = creator.id

        acervo = schema.load(request.json)
        db.session.add(acervo)

        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))

        return schema.dump(acervo), 201

    ''' Pega todos arquivos do banco de dados '''
    def get(self):
        schema = FileSchema(many = True)

        title = request.args.get('title')
        type = request.args.get('type')
        min_click_quantity = request.args.get('min_click')
        max_click_quantity = request.args.get('max_click')
        category = request.args.get('category')
        area = request.args.get('area')
        min_year = request.args.get('min_year')
        max_year = request.args.get('max_year')
        awarded = request.args.get('awarded')
        tag_list = request.args.get('tags')
        try:
            tag_list = json.loads(tag_list)
        except:
            #tag_list = None
            tags_list = None
        
        filter_list = []
        if(title):
            title = f'%{title}%'
            filter_list.append(File.title.ilike(title))
        if(type):
            filter_list.append(File.type == type)
        if(min_click_quantity):
            filter_list.append(File.click_quantity >= min_click_quantity)
        if(max_click_quantity):
            filter_list.append(File.click_quantity <= max_click_quantity)
        if(category):
            category = f'%{category}%'
            filter_list.append(File.category.ilike(category))
        if(area):
            area = f'%{area}%'
            filter_list.append(File.area.ilike(area))
        if(min_year):
            filter_list.append(File.year >= min_year)
        if(max_year):
            filter_list.append(File.year <= max_year)
        if(awarded):
            awarded = f'%{awarded}%'
            filter_list.append(File.awarded.ilike(awarded))
        if(tag_list != None):
            filter_list.append(File.tags_associated.any(Tag.id.in_(tag_list)))
        
        query = File.query
        for choosen_filter in filter_list:
            query = query.filter(choosen_filter)
        return jsonify(schema.dump(File.query.all())),200

# /file/<int:id>
class FileDetails(MethodView):

    ''' Altera dados de arquivo especifico '''
    def patch(self, id):
        file = File.query.get_or_404(id)
        schema = FileSchema()
        file = schema.load(request.json, instance=file, partial = True)
        data = request.json

        author_id = data.pop('author', None)
        creator_id = data.pop('creator', None)
        tag_id = data.pop('tag', None)

        file = schema.load(data, instance=file, partial = True)
        
        # Association
        if(author_id != None):
            file.authors_associated = []
            for id in author_id:
                author = Author.query.get(id)
                file.authors_associated.append(author)

        if(tag_id != None):
            file.tags_associated = []
            for id in tag_id:
                tag = Tag.query.get(id)
                file.tags_associated.append(tag)

        if(creator_id != None):
            creator = User.query.get(creator_id)
            file.creator_id = creator.id

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

        file.click_quantity += 1
        file.save()

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
    
    #/file/top-access
class TopAccess(MethodView):
    def get(self):
        schema = FileSchema(many = True)
        files = File.query.order_by(File.click_quantity.desc()).limit(10).all()

        return schema.dump(files),200