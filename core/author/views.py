from flask import Blueprint, render_template
from core.models import Author


authors_app = Blueprint(
    "authors_app", 
    __name__,
    static_folder='../static',
    url_prefix='/authors')

@authors_app.route("/")
def authors_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)
