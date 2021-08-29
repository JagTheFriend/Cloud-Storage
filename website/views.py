from . import log
from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    log.debug("Received a GET request at `/home`")
    return render_template("home.html")
