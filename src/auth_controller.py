from db_shared import db, DBController
from flask_login import login_user, logout_user

class AuthController(DBController):
    db = db

    @classmethod
    def register(cls, user):
        cls.db.session.add(user)
        cls.db.session.commit()

    @staticmethod
    def login(user):
        return login_user(user)

    @staticmethod
    def logout():
        # Always returns true
        return logout_user()