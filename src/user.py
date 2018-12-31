from db_shared import db
from flask_login import UserMixin
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

class User(UserMixin, db.Model):
    __tablename__ = "user"

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def create(email, password):
        hashed_password = generate_password_hash(password)
        user_args = {"email": email, "password": hashed_password}
        return User(**user_args)