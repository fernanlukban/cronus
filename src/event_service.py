from flask import Blueprint, render_template, abort

event_service_page = Blueprint('event_service_page', __name__, template_folder='templates')

@event_service.record
def setup_(state):


@event_service_page.route('/')
def index():
    return "hello!"