from flask.views import MethodView
from flask import request
from app.storageDireto.storage import storage
import uuid

# /direto/upload/media
class UploadMedia(MethodView):
    ''' Cria um arquivo no storage '''
    def post(self):
        media = request.files.get('media')
        if not media:
            return {'erro' : 'arquivo não enviado'}, 400

        media_format = request.args.get('media_format')
        if not media_format:
            return {'erro' : 'formato do arquivo não especificado'}, 400

        media_path = f'{uuid.uuid4().hex}.{media_format}'
        response = storage.upload_file(file_key=media_path, file=media, file_format=media_format)

        if not response[0]:
            return {'erro' : response[1]}, 400
        
        return {'media_path' : media_path}, 200



# presigned/media/<string:file_name>
class DiretoStorage(MethodView):
    
    ''' Retorna um arquivo do storage '''
    def get(self, file_name):

        response = storage.get_url(file_key=file_name)
        if not response:
            return {'erro' : response}, 400
        
        return {'URL': response}, 200

    def delete(self, file_name):
        storage.delete_object(file_key=file_name)
        return {'msg':'Arquivo deletado com sucesso!'}, 200