from db_shared import db, DBController
from user import User

class UserController(DBController):
    db = db

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def register(cls, email, password):
        user = User.create(email, password)
        cls.db.session.add(user)
        cls.db.session.commit()