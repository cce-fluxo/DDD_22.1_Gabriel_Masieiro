from flask import Blueprint
from app.storageDireto.controller import UploadMedia, DiretoStorage

storageDireto_api = Blueprint('storageDireto_api',__name__)

storageDireto_api.add_url_rule('/direto/upload/media', 
                                view_func=UploadMedia.as_view('upload_media_presigned'), 
                                methods=['POST'])
                
storageDireto_api.add_url_rule('/direto/media/<string:file_name>', 
                                view_func=DiretoStorage.as_view('media_presigned'), 
                                methods=['GET', 'DELETE'])