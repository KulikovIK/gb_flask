from flask import Flask

from .index.views import index
from .user.views import users_app
from .articles.views import articles_app
from core.models.database import db
from core.auth.view import login_manager, auth_app


VIEWS = [
    index,
    users_app,
    articles_app,
    auth_app,
]

def make_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    register_blueprints(app)
    app.config["SECRET_KEY"] = "abcdefg123456"
    login_manager.init_app(app)
    return app

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
