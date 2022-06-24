# Developped by Thomas McDonald in collaboration with Mathys Marcouiller
# GitHub: https://github.com/ThomasMcDonald904

import json
import requests
import urllib.parse

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
    data = {"waypoints": [point for point in waypoints], "options": {"travelMode": "car", "vehicleCommercial": False, "waypointConstraints": {"originIndex": 0}}}
    json_data = json.loads(data)
    return json_data

def get_route(json_data, api_key=tomtom_api_key):
    api_call_route = f"https://api.tomtom.com/routing/waypointoptimization/1?key={api_key}"
    response = requests.post(api_call_route, json_data)
    data = response.json()
    return data

