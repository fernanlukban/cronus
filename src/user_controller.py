from db_shared import DBController
from user import User

class UserController(DBController):

    @classmethod
    def get_by_id(user_id):
        return User.get(user_id)