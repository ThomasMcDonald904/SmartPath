from flask import Flask, render_template
from requests import request

from routing_management import *


app = Flask(__name__, template_folder='templates/')


@app.route("/")
def home():
    print(get_route(address_to_lonlat("904 rue Arthur-McNicoll", "Shawinigan"), address_to_lonlat("1029 rue Notre-Dame", "Champlain")))
    return render_template("home.html")

@app.route("/route_submit", methods=["GET", "POST"])
def rounting_form():
    if request.method == "POST":
        pass
    