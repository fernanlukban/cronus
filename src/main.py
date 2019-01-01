from auth_shared import login_manager
from db_shared import db
from event_controller import EventController
from event_service import event_service_page
from flask import Flask
from auth_service import auth_service_page

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