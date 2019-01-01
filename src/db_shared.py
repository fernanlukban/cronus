from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DBController:
    db = db

class DBNotFoundError(Exception):
    pass