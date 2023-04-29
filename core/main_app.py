from flask import Flask
from flask_migrate import Migrate

from core.index.views import index
from core.user.views import users_app
from core.articles.views import articles_app
from core.models.database import db
from core.auth.view import login_manager, auth_app
from core.security import flask_bcrypt
from core.author.views import authors_app



VIEWS = [
    index,
    users_app,
    articles_app,
    auth_app,
    authors_app,
]

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)

app = Flask(__name__)
app.config.from_object(f"core.config.Config")

db.init_app(app)

migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

register_blueprints(app)
app.config["SECRET_KEY"] = "abcdefg123456"

login_manager.init_app(app)
flask_bcrypt.init_app(app)
