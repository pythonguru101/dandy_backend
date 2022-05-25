from ast import Str
import json
from typing import Dict
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
    This is responsible for receiving wifi connection data and geofence location
    and exporting it to a json file

    Method Type:
        _type_: Post

    Args for Post Request:
        wifi_connection_data (str) : data to connect with wifi
        geofence_location (str): geofence location data

    Raises:
        Exception: raise exception if anything fails
    """
    if request.method == "POST":
        try:
            wifi_connection_data = request.json.get("wifi_connection_data")
            geofence_location = request.json.get("geofence_location")

            if not wifi_connection_data or not geofence_location:
                return jsonify(
                    {
                        "StatusCode": 400,
                        "message": "Please provide wifi connection data and geofence location",
                    }
                )

            jsonable_data = {
                "wifi": wifi_connection_data,
                "geofence_location": geofence_location,
            }

            write_json(
                json_serializable_data=jsonable_data, filename="store_house.json"
            )

            return jsonify(
                {"StatusCode": 200, "message": "Data has been successfully stored"}
            )
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
