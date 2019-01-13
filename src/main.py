from .shared.auth import login_manager
from .shared.db import db
from .event.controller import EventController
from .event.service import event_service_page
from flask import Flask
from .auth.service import auth_service_page

app = Flask(__name__)

app.config["SECRET_KEY"] = "swaglord420"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cronus:cronus@localhost/cronus'
# To suppress a deprecated setting warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(event_service_page)

app.register_blueprint(auth_service_page)

if __name__ == '__main__':
    app.run()