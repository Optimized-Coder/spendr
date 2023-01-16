from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(55), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    balance = db.Column(db.String)