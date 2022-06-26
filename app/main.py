from flask import Flask, render_template, request
import routing_management
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='templates/')
CORS(app)

@cross_origin
@app.route("/")
def home():
    return render_template("home.html")


@cross_origin
@app.route("/route_submit", methods=["GET", "POST"])
def routing_form():
    starting_address = request.form.get("is_starting_destination")
    temp_form = list(request.form.items())
    temp_form = [item for item in temp_form if not item[0] == "is_starting_destination" and not item[0] == "Enter"]
    length = len(temp_form)
    address_city_pairs = [[temp_form[i][1], temp_form[i+1][1]] for i in range(0, length-1, 2)] 

    for pair in address_city_pairs:
        if pair[0] == starting_address:
            starting_address = [starting_address, pair[1]]

    address_city_pairs.remove(starting_address)
    address_city_pairs.insert(0, starting_address)

    waypoint_list = []
    for pair in address_city_pairs:
        waypoint_list.append(routing_management.address_to_lonlat(pair[0], pair[1]))

    json_data = routing_management.generate_waypoints_json(*waypoint_list)

    with open('tempdata/json_waypoints.json', 'w') as json_file:
        json_file.write(json_data)

    with open("tempdata/json_waypoints.json", "r") as json_file:
        route = routing_management.get_route(json_file)

    return route
    