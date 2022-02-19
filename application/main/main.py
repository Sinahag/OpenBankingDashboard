import os
from flask import render_template, Blueprint

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def index():
    return render_template("index.html",index=True, title="Home")