from flask import Flask, render_template, request
from routing_management import *


app = Flask(__name__, template_folder='templates/')


@app.route("/")
def home():
    # print(get_route(address_to_lonlat("904 rue Arthur-McNicoll", "Shawinigan"), address_to_lonlat("1029 rue Notre-Dame", "Champlain")))
    return render_template("home.html")


@app.route("/route_submit", methods=["GET", "POST"])
def routing_form():
    print(request.form)
    
    # address_list = []
    # for i in request.form:
    #     address_list.append(request.form.get(i))
    # address_list.remove("Submit")
    
    # Make this render good thing
    return render_template("home.html")
    