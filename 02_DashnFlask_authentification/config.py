from os import path,environ
import dotenv
from datetime import timedelta


# Database initialization
basedir = path.abspath(path.dirname(__file__))
dotenv.load_dotenv(path.join(basedir, '.env'))

class Config:
    """base config : commun params"""
    SECRET_KEY = environ.get('SECRET_KEY')
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    FLASK_APP='dashflask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    FLASK_ENV='development'
    FLASK_DEBUG=True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

class ProdConfig(Config):
    FLASK_ENV='production'
    FLASK_DEBUG=False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)