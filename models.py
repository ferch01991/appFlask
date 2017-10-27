# aqui se representaran los modelos. Flask-SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug import generate_password_hash 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(60))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)


    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email



    def __create_password(self, password):
        return generate_password_hash(password)
