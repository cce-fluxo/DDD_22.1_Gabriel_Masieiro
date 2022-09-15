from flask.views import MethodView
from flask import request
from app.storagePreSigned.storage import storage
import uuid

# /presigned/upload/media
class UploadMedia(MethodView):
    ''' Cria um arquivo no storage'''
    def get(self):

        media_format = request.args.get('media_format')
        if not media_format:
            return {'erro' : 'formato do arquivo não especificado'}, 400

        media_path = f'{uuid.uuid4().hex}.{media_format}'
        url = storage.put_url(file_key=media_path)
        
        return {'media_url' : url, 'media_path':media_path}, 200

# presigned/media/<string:file_name>
class PresignedStorage(MethodView):
    
    ''' Retorna um arquivo do storage '''
    def get(self, file_name):
        
        response = storage.get_url(file_key=file_name)
        if not response:
            return {'erro' : response}, 400
        
        return {'URL': response}, 200

    def delete(self, file_name):
        storage.delete_object(file_key=file_name)
        return {'msg':'Arquivo deletado com sucesso!'}, 200