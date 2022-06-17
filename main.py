from flask import Flask, render_template
from requests import request

import routing_management


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/route_submit", methods=["GET", "POST"])
def rounting_form():
    if request.method == "POST":
        pass
    