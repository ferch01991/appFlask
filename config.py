import os

class Config(object):
    SECRET_KEY = 'my_secret_key'

# configuraciones para el entorno de desarrollo 
class DevelopmentConfig(Config):
    DEBUG = True
    # pip install MySQL-Python, pymysql 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
