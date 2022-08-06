import os
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = D:\protected_resources\microblog

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret-Key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# print(Config.SQLALCHEMY_DATABASE_URI)