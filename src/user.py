from db_shared import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)