import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'