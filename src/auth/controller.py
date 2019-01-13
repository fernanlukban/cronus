from ..shared.db import db, DBController
from flask_login import login_user, logout_user

class AuthController(DBController):
    @staticmethod
    def register(user):
        DBController.db.session.add(user)
        DBController.db.session.commit()

    @staticmethod
    def login(user):
        return login_user(user)

    @staticmethod
    def logout():
        # Always returns true
        return logout_user()