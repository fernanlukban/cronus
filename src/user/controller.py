from ..shared.db import db, DBController
from .user import User

class UserController(DBController):
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(email, password):
        return User.create(email, password)