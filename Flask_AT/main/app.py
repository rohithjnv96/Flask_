# refactor imports
from flask import *
from Flask_AT.main.forms import SignUpForm

main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    return render_template("home.html")


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit() and request.method == 'POST':
        return "Almost logged in"
    return render_template("signup_page.html", form=form)


@main.route('/register_user', methods=['POST'])
def register_user():
    return f'{request.form["username"]} -> {request.form.get("email")}'
