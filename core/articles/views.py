from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint(
    'articles_app',
    __name__,
    static_folder='../static',
    url_prefix='/articles')

ARTICLES = {
    1: "Flask", 
    2: "Django", 
    3: "JSON:API"
    }

@articles_app.route("/")
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)

@articles_app.route("/<int:acticle_id>/")
def article_details(acticle_id: int):

    try:
        article_name = ARTICLES[acticle_id]
    except KeyError:
        raise NotFound(f"Статья #{acticle_id} не существует!")
    
    return render_template('articles/details.html', acticle_id=acticle_id, article_name=article_name)
