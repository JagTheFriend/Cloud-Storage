from . import log
from flask.helpers import flash, url_for
from flask_login.utils import login_user
from flask import Blueprint, render_template, request
from flask_login import login_user, current_user

from website.models import User
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    # log.debug("Received a GET request at `/home`")
    # return render_template("home.html")
    if request.method == "POST":
        log.debug("Received a POST request on `/login`")

        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                log.info("Logged in")
                flash("Logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect.", category="error")
        else:
            flash("Email does not exists.", category="error")

    log.debug("Received GET request on `/login`")
    return render_template("login.html", user=current_user)
