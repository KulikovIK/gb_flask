from flask import Flask

from .index.views import index
from .user.views import users_app
from .articles.views import articles_app


VIEWS = [
    index,
    users_app,
    articles_app,
]

def make_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
