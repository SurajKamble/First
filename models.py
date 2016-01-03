from flask_sqlalchemy import SQLAlchemy
from __init__ import app


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.column(db.String)
    lastName = db.column(db.String)
    username = db.Column(db.String, unique=False)
    password = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, firstName, lastName, email):
        self.username = username
        self.password = password