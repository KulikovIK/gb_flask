import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
