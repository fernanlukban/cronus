from auth_shared import login_manager
from db_shared import DBNotFoundError
from flask import (
    abort,
    Blueprint,
    current_app,
    render_template
)
from user_controller import UserController

auth_service_page = Blueprint("auth_service_page", __name__, template_folder="templates")

@login_manager.user_loader
def user_loader(user_id):
    return UserController.get_by_id(user_id)