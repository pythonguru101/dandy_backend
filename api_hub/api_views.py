# © 2022, Dandy technology LLC

from ast import Str
import json
import socket
import os
from shlex import quote
from urllib import response
import subprocess
from flask import Blueprint, request, jsonify

from api_hub import update

api_views = Blueprint("api_views", __name__)


def write_json(json_serializable_data: dict, filename: Str) -> None:
    """
    This is responsible for storing data in a json file

    Args:
        json_serializable_data (dict): data which is subject to be stored in a json file
        filename (Str): file where data will be stored

    Raises:
        Exception: raise exception in case it fails to store
    """
    try:
        json_object = json.dumps(json_serializable_data, indent=4)
        with open(filename, "w") as outfile:
            outfile.write(json_object)
    except:
        raise Exception("Could not save data in json file")


# this is for pinging the server
@api_views.route("/", methods=["GET"])
def ping():
    """
    This is responsible for pinging the server

    Returns:
        str: returns a string "pong"
    """
    response = {
                "message": "Available", 
                "status": "success", 
                "StatusCode": 200,
                "ip": socket.gethostbyname(socket.gethostname()),
                "device": {
                    "id": "Abc123",
                    "name": "dandy_robot_5000",
                    "serial_number":"5000",
                    "type": "Micro Controller",
                    "status": "running",
                    "connection_status": "connected",
                    "connected_ssid": "458940",
                    "battery_level": "Highly Charged",
                    "storage_level": "Full",
                },
                }
    
    return jsonify(response)


@api_views.route("/connect-with-robot", methods=["POST"])
def connect_with_robot():
    """
    This is responsible for receiving robot connection data and exporting it to a json file

    Method Type:
        _type_: Post

    Args for Post Request:
        ssid (str) : SSID data
        password (str) : Password

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "POST":
        try:
            if not request.data:
                raise Exception("Valid data is required")

            ssid = request.json.get("ssid", None)
            password = request.json.get("password", None)

            if not ssid:
                raise Exception("SSID is required")
            if not password:
                raise Exception("Password is required")

            if "dandy-robot" in socket.gethostname():
                command = 'nmcli dev wifi connect "{}" password "{}" ifname wlan0'.format(
                    quote(ssid), quote(password)
                )  # quote escapes string to avoid security risk
                # print(command)
                return_val = os.system(command)

                if return_val != 0:
                    raise Exception(
                        "Unable to connect to wifi network with these credentials"
                    )

            # todo remove json output for production
            jsonable_data = {"ssid": ssid, "password": password}
            write_json(
                json_serializable_data=jsonable_data,
                filename="store_robot_connection_data.json",
            )

            response = {
                "StatusCode": 200,
                "message": "Successfully connected",
                "device": {
                    "id": "Abc123",
                    "name": "Robot Micro",
                    "serial_number":"5000",
                    "type": "Micro Controller",
                    "status": "running",
                    "connection_status": "connected",
                    "connected_ssid": "458940",
                    "battery_level": "Highly Charged",
                    "storage_level": "Full",
                },
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})


@api_views.route("/robot-location-fencing", methods=["POST"])
def robot_location_fencing():
    """
    This is for fencing robot location

    Method Type:
        _type_: Post

    Args for Post Request:
        coordinates (array) : array of object containing latitude and longitude
        holes (array) : array of object containing latitude and longitude

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "POST":
        try:
            if not request.data:
                raise Exception("Valid data is required")

            fencing_location = request.get_json()

            write_json(
                json_serializable_data=fencing_location,
                filename="store_fencing_data.json",
            )


            if "dandy-robot" in socket.gethostname():
                os.makedirs("/home/mendel/settings/", exist_ok=True)
                raw_geofence_filepath = "/home/mendel/settings/geofence_raw.csv"

                with open(raw_geofence_filepath, "w") as f:
                    for i in fencing_location["coordinates"]:
                        lat = i["latitude"]
                        lon = i["longitude"]
                        f.write(str(lat) + "," + str(lon) + "\n")

                command = "ros2 service call /update_geofence std_srvs/srv/Trigger {}"
                subprocess.call(command.split(" "))


            response = {
                "StatusCode": 200,
                "message": "Data successfully stored",
                "coordinates": [
                    {"latitude": 23.2332, "longitude": 23.2332},
                    {"latitude": 23.2332, "longitude": 23.2332},
                ],
                "holes": [
                    {"latitude": 23.2332, "longitude": 23.2332},
                    {"latitude": 23.2332, "longitude": 23.2332},
                ],
                "id": 0,
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})


@api_views.route("/get-robot-current-location", methods=["GET"])
def robot_current_location():
    """
    This is responsible for retrieving robot location

    Method Type:
        _type_: Get

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "GET":
        try:
            response = {
                "StatusCode": 200,
                "message": "Successfully data retreived",
                "device": {
                    "id": "Abc123",
                    "name": "Robot Micro",
                    "serial_number":"5000",
                    "type": "Micro Controller",
                    "status": "running",
                    "connection_status": "connected",
                    "connected_ssid": "458940",
                    "battery_level": "Highly Charged",
                    "storage_level": "Full",
                },
                "coordinates": {"latitude": 40.730610, "longitude": -73.953242},
                "malfunction": {
                    "wheel_1": True,
                    "wheel_2": True,
                    "wheel_3": True,
                    "wheel_4": True,
                    "sensor": True,
                    "motor": True,
                    "clipper": True,
                },
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})


@api_views.route("/check-update", methods=["GET"])
def check_update() -> object:
    """
    This is to check any available update

    Returns:
        object: response containing status code and a boolean field
    """
    if request.method == "GET":
        is_available = False
        if "dandy-robot" in socket.gethostname():
            new_version = update.checkForUpdate()
            print(new_version)
            is_available = new_version is not None
        try:
            response = {"StatusCode": 200, "is_available_update": is_available}
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})


@api_views.route("/update-software", methods=["POST"])
def update_software() -> object:
    """
    This is to push software update available indication

    Args for Post Request:
        is_update_available (bool) :True or False

    Returns:
        object: response containing status and message
    """
    if request.method == "POST":
        try:
            if not request.data:
                raise Exception("Valid data is required")

            is_update_available = request.json.get("is_update_available", None)
            if not is_update_available:
                raise Exception("is_update_available field is required")

            jsonable_data = {"is_update_available": is_update_available}

            write_json(
                json_serializable_data=jsonable_data,
                filename="software_update_available.json",
            )

            if "dandy-robot" in socket.gethostname():
                download_success = update.downloadUpdate()
                if download_success:
                    update.applyDownloadedUpdate()

            response = {
                "StatusCode": 200,
                "message": "Software update available data successfully passed",
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
