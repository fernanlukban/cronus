from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DBController:
    pass

class DBNotFoundError(Exception):
    pass