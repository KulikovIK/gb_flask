from flask import Flask
from flask_migrate import Migrate

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

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)

app = Flask(__name__)
app.config.from_object(f"core.config.Config")

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/core.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db, compare_type=True)

register_blueprints(app)
app.config["SECRET_KEY"] = "abcdefg123456"

login_manager.init_app(app)
