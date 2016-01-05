from flask_sqlalchemy import SQLAlchemy
from __init__ import app


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    password1 = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password2 = db.Column(db.String)
    tags = db.relationship('Tags', backref='user', lazy='dynamic')

    def __init__(self,  password1, firstName, lastName, email, password2):
        self.email = email
        self.password1 = password1
        self.firstName = firstName
        self.lastName = lastName
        self.password2 = password2


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, tag_name, user=None):
        self.tag_name = tag_name
        self.user = user


class CsTags(Tags):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag_name = db.Column(db.String)

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self.tag_name = tag_name


class MusicTags(Tags):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag_name = db.Column(db.String)

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self.tag_name = tag_name


class GamingTags(Tags):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag_name = db.Column(db.String)

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self.tag_name = tag_name


class ElecTags(Tags):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag_name = db.Column(db.String)

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self.tag_name = tag_name


class TagsClicked(Tags):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag_name = db.Column(db.String)

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self.tag_name = tag_name