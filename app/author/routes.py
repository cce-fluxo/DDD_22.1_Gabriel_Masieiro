from flask import Blueprint
from app.author.controller import AuthorsAll, AuthorDetails, AuthorCreate


author_api = Blueprint("author_api", __name__)

author_api.add_url_rule("/autor/create", view_func=AuthorCreate.as_view("authorCreate"), methods=["POST"])
author_api.add_url_rule("/autores", view_func=AuthorsAll.as_view("authorsAll"), methods=["GET"])
author_api.add_url_rule("/autor/<int:author_id>", view_func=AuthorDetails.as_view("authorsDetails"), methods=["GET", "DELETE"])