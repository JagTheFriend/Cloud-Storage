from . import DATABASE, log
import os
from flask import Blueprint, render_template, flash
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
    if os.path.isdir(f"{DATABASE}\\{username}"):
        os.chdir(f"{DATABASE}\\{username}")
        files = {i: f"{DATABASE}\\{username}\\{i}" for i in os.listdir()}
    else:
        # creating the folder
        os.mkdir(f"{DATABASE}/{username}")
    return files


@views.route("/get_file/filename=<filename>&username=<username>")
@login_required
def get_specific_file(filename: str, username: str):
    if os.path.isdir(f"{DATABASE}\\{username}"):
        os.chdir(f"{DATABASE}\\{username}")
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                return file.read()
    else:
        flash("File not found!", category="error")
