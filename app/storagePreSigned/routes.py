from flask import Blueprint
from app.storagePreSigned.controller import UploadMedia, PresignedStorage

storagePreSigned_api = Blueprint('storagePreSigned_api',__name__)

storagePreSigned_api.add_url_rule('/presigned/upload/media', 
                                view_func=UploadMedia.as_view('upload_media_presigned'), 
                                methods=['GET'])
                
storagePreSigned_api.add_url_rule('/presigned/media/<string:file_name>', 
                                view_func=PresignedStorage.as_view('media_presigned'), 
                                methods=['GET', 'DELETE'])