from flask import (
    abort,
    Blueprint,
    current_app,
    render_template
)
from db_shared import DBNotFoundError

event_service_page = Blueprint("event_service_page", __name__, template_folder="templates")

@event_service_page.route('/')
def index():
    return "hello!"