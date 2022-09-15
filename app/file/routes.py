from flask import Blueprint
from app.file.controller import FileAll, FileDetails

file_api = Blueprint("file_api", __name__)

file_api.add_url_rule("/file", view_func=FileAll.as_view("allFiles"), methods=["POST", "GET"])
file_api.add_url_rule("/file/<int:id>", view_func=FileDetails.as_view("filesDetails"), methods=["PATCH", "GET", "DELETE"])