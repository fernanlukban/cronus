from db_shared import db, DBController
from user import User

class UserController(DBController):
    db = db

    @staticmethod
    def get_by_id(user_id):
        return User.get(user_id)

    @classmethod
    def register(cls, user):
        cls.db.session.add(user)
        cls.db.session.commit()