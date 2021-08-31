from . import DATABASE, log
import os
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    log.debug("Received a GET request at `/home`")
    return render_template("home.html", user=current_user)


@views.route("/files?username=<string:username>")
def get_files(username: str):
    # check whether the folder already exists
    if os.path.isdir(f"{DATABASE}/{username}"):
        return "<h1> yes </h1>"
    else:
        # creating the folder
        os.mkdir(f"{DATABASE}/{username}")
