from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # max length of 150 characters, and it must be unique
    username = db.Column(db.String(150), unique=True)  # username
    password = db.Column(db.String(150))  # doesn't need to be unique
