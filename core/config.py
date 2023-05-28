import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="abcdefg123456"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
