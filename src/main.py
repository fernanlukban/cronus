from auth_shared import login_manager
from db_shared import db
from event_controller import EventController
from event_service import event_service_page
from flask import Flask

app = Flask(__name__)
db.init_app(app)
login_manager.init_app(app)

app.config["event_controller"] = EventController()
app.register_blueprint(event_service_page)

if __name__ == '__main__':
    app.run()