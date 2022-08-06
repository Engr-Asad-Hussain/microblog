from json import load
import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = D:\protected_resources\microblog

load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret-Key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['asad.h1998@yahoo.com']

# print(Config.SQLALCHEMY_DATABASE_URI)