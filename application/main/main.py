import os
from flask import render_template, Blueprint
# from flask_login import login_required
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@main.route("/index")
# @login_required
def index():
    return render_template("index.html", index=True)


@main.route("/dashboard")
# @login_required
def dashboard():
    return render_template("dashboard.html", username='User')

# create the follow up pages for the dashboard (where the dashboard leadas to)
