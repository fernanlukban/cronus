from auth_controller import AuthController
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
from flask_login import login_required
from form_login import FormLogin
from form_register import FormRegister
from user_controller import UserController
from sqlalchemy.exc import IntegrityError

auth_service_page = Blueprint("auth_service_page", __name__, template_folder="../templates")

def is_safe_url(target):
    # ref_url = urlparse(request.host_url)
    # test_url = urlparse(urljoin(request.host_url, target))
    # return test_url.scheme in ('http', 'https') and \
    #        ref_url.netloc == test_url.netloc
    return True

@login_manager.user_loader
def user_loader(email):
    return UserController.get_by_email(email)

@auth_service_page.route("/logged_in")
@login_required
def logged_in():
    return "Logged in!"

@auth_service_page.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        email = form_login.email.data
        password = form_login.password.data
        user = UserController.get_by_email(email)
        if user is None:
            print("No user found!")
            flash("No user found!")
        if not user.check_password(password):
            print("Invalid password!")
            flash("Invalid password!")
        if AuthController.login(user):
            flash("Login successful")
        print(user, password)       
        return redirect(url_for('auth_service_page.logged_in'))
    return render_template('form_login.html', form=form_login)

@auth_service_page.route("/register", methods=["GET", "POST"])
def register():
    form_register = FormRegister()
    if form_register.validate_on_submit():
        email = form_register.email.data
        password = form_register.password.data
        try:
            new_user = UserController.create(email, password)
            AuthController.register(new_user)
        except IntegrityError:
            return "Already signed up!"
        flash("Signed up!")

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(url_for("auth_service_page.register"))
    else:
        return render_template('form_register.html', form_register=form_register)

@auth_service_page.route('/logout')
@login_required
def logout():
    AuthController.logout()
    return redirect(url_for("auth_service_page.login"))