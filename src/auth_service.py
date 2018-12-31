from auth_shared import login_manager
from db_shared import DBNotFoundError
from flask import (
    abort,
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from form_login import FormLogin
from form_register import FormRegister
from user_controller import UserController

auth_service_page = Blueprint("auth_service_page", __name__, template_folder="../templates")

def is_safe_url(target):
    # ref_url = urlparse(request.host_url)
    # test_url = urlparse(urljoin(request.host_url, target))
    # return test_url.scheme in ('http', 'https') and \
    #        ref_url.netloc == test_url.netloc
    return True

@login_manager.user_loader
def user_loader(user_id):
    return UserController.get_by_id(user_id)

@auth_service_page.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    return render_template('form_login.html', form=form_login)

@auth_service_page.route("/register", methods=["GET", "POST"])
def register():
    form_register = FormRegister()
    if form_register.validate_on_submit():
        email = form_register.email.data
        password = form_register.password.data
        UserController.register(email, password)
        flash("Signed up!")

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(url_for("auth_service_page.register"))
    return render_template('form_register.html', form_register=form_register)