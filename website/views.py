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


@views.route("/files/username=<username>")
@login_required
def get_files(username: str):
    # check whether the folder already exists
    files = {}
    if os.path.isdir(f"{DATABASE}/{username}"):
        os.chdir(f"{DATABASE}/{username}")
        files = {i: f"{DATABASE}/{username}/{i}" for i in os.listdir()}
    else:
        # creating the folder
        os.mkdir(f"{DATABASE}/{username}")
    return files
