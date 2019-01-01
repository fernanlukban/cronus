from db_shared import db, DBController
from user import User

class UserController(DBController):
    db = db

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def create(cls, email, password):
        return User.create(email, password)