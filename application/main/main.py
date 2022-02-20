import os
from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@main.route("/index")
def index():
    return render_template("index.html", index=True)


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", username='User')

# create the follow up pages for the dashboard (where the dashboard leadas to)
