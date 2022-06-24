from flask import Flask, render_template, request
from routing_management import *


app = Flask(__name__, template_folder='templates/')


@app.route("/")
def home():
    # print(get_route(address_to_lonlat("904 rue Arthur-McNicoll", "Shawinigan"), address_to_lonlat("1029 rue Notre-Dame", "Champlain")))
    return render_template("home.html")


@app.route("/route_submit", methods=["GET", "POST"])
def routing_form():
    starting_address = request.form.get("is_starting_destination")
    temp_form = list(request.form.items())
    # print(temp_form)
    temp_form = [item for item in temp_form if not item[0] == "is_starting_destination" and not item[0] == "Enter"]
    length = len(temp_form)
    address_city_pairs = [[temp_form[i][1], temp_form[i+1][1]] for i in range(0, length-1, 2)] 

    waypoint_list = []
    for pair in address_city_pairs:
        waypoint_list.append(address_to_lonlat(pair[0], pair[1]))
    
    print(waypoint_list)

    # json_data = generate_waypoints_json()

    return render_template("login.html")
    