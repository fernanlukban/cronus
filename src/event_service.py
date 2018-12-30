from flask import (
    abort,
    Blueprint,
    current_app,
    render_template
)

event_service_page = Blueprint('event_service_page', __name__, template_folder='templates')

@event_service_page.record
def setup_(state):
    pass

@event_service_page.route('/')
def index():
    return "hello!"