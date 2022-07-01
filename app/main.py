from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json
import requests
import urllib.parse


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
        waypoint_list.append(address_to_lonlat(pair[0], pair[1]))

    json_data = generate_waypoints_json(*waypoint_list)

    # with open(r"app\tempdata\json_waypoints.json", "w+") as json_file:
    #     json_file.write(json_data)

    # with open(r"app\tempdata\json_waypoints.json", "r") as json_file:
    #     route = get_route(json_file)
    route = get_route(json_data)

    return route


# ----------------------------
# Libraries
# ----------------------------

tomtom_api_key = "NGGuMr6A0UbNGS8ZB1egkfviHxZ4ki2W"



def address_to_lonlat(_address: str, _city: str, api_key=tomtom_api_key):
    url_encoded_address = urllib.parse.quote(_address)
    api_call_geocode = f"https://api.tomtom.com/search/2/geocode/{url_encoded_address}.json?storeResult=false&countrySet=Canada&view=Unified&key={api_key}"

    response = requests.request("GET", api_call_geocode)
    data = response.json()
    for i in data["results"]:
        if i["type"] == "Point Address" and i["address"]["municipality"] == _city:
            user_address_lon_lat = i["position"]

    # formatted_lon_lat = urllib.parse.quote(f"{user_address_lon_lat['lat']},{user_address_lon_lat['lon']}")
    # return user_address_lon_lat['lat'], user_address_lon_lat['lon']
    return {"point": {"latitude": user_address_lon_lat["lat"], "longitude": user_address_lon_lat["lon"]}}


def lon_lat_to_address(lon_lat_dict, api_key=tomtom_api_key):
    lon_lat_pair = ",".join([str(lon_lat_dict["latitude"]), str(lon_lat_dict["longitude"])])
    lon_lat_pair_encoded = urllib.parse.quote(lon_lat_pair)
    api_call_reverse_geocode = f"https://api.tomtom.com/search/2/reverseGeocode/crossStreet/{lon_lat_pair_encoded}.json?returnSpeedLimit=false&radius=10000&returnRoadUse=false&callback=cb&allowFreeformNewLine=false&returnMatchType=false&view=Unified&key={api_key}"
    response = requests.request("GET", api_call_reverse_geocode)
    data = response.json()
    return data

def generate_waypoints_json(*waypoints):
    # data = {"waypoints": [point for point in waypoints], "options": {"travelMode": "car", "vehicleCommercial": False, "waypointConstraints": {"originIndex": 0}}}
    data = {"waypoints": [point for point in waypoints], "options": {"travelMode": "car", "vehicleCommercial": False}}
    json_data = json.dumps(data, indent=4)
    return json_data

def get_route(json_data, api_key=tomtom_api_key):
    api_call_route = f"https://api.tomtom.com/routing/waypointoptimization/1?key={api_key}"
    response = requests.post(api_call_route, data=json_data)
    data = response.text
    return data


