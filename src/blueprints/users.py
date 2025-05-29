from flask import jsonify, Blueprint
from ..commands.ping import Ping
from ..commands.reset_data import ResetData

users_blueprint = Blueprint("users", __name__)


@users_blueprint.get("/users/ping")
def ping():
    return jsonify(Ping().execute())


@users_blueprint.post("/users/reset")
def reset_data():
    reset_data = ResetData()
    reset_data.execute()
    return jsonify({"mssg": "Todos los datos fueron eliminados"}), 200

