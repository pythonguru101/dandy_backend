from ast import Str
import json
from flask import (
    Blueprint,
    request,
    jsonify,
)

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


@api_views.route("/connect-with-robot", methods=["POST"])
def connect_with_robot():
    """
    This is responsible for receiving wifi connection data and exporting it to a json file

    Method Type:
        _type_: Post

    Args for Post Request:
        wifi_connection_data (str) : data to connect with wifi

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "POST":
        try:
            if not request.data :
                raise Exception ("Valid data is required")

            wifi_connection_data = request.json.get("wifi_connection_data",None)

            if not wifi_connection_data:
                raise Exception ("Wifi connection data is required")

            jsonable_data = {"wifi": wifi_connection_data}

            write_json(
                json_serializable_data=jsonable_data,
                filename="store_wifi_connection_data.json",
            )
            return jsonify(
                {
                    "StatusCode": 200,
                    "message": "Wifi connection data has been successfully stored",
                }
            )
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})


@api_views.route("/robot-geofence-location", methods=["POST"])
def robot_geofence_location():
    """
    This is responsible for receiving geofence location
    and exporting it to a json file

    Method Type:
        _type_: Post

    Args for Post Request:
        geofence_location (str): geofence location data

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "POST":
        try:
            if not request.data :
                raise Exception ("Valid data is required")

            geofence_location = request.json.get("geofence_location",None)

            if not geofence_location:
                raise Exception ("Geofence location data is required")

            jsonable_data = {"geofence_location": geofence_location}

            write_json(
                json_serializable_data=jsonable_data,
                filename="store_geofence_location.json",
            )

            return jsonify(
                {
                    "StatusCode": 200,
                    "message": "Geofence location data has been successfully stored",
                }
            )
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
