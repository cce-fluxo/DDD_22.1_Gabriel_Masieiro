from flask import Blueprint
from app.tag.controller import TagAll, TagDetails, TagCreate


tag_api = Blueprint("tag_api", __name__)

tag_api.add_url_rule("/tag/create", view_func=TagCreate.as_view("tagCreate"), methods=["POST"])
tag_api.add_url_rule("/tags", view_func=TagAll.as_view("tagsAll"), methods=["GET"])
tag_api.add_url_rule("/tag/<int:tag_id>", view_func=TagDetails.as_view("tagsDetails"), methods=["GET", "DELETE"])