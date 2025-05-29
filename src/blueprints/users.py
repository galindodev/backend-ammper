from flask import jsonify, Blueprint, request
from ..commands.ping import Ping
from ..commands.reset_data import ResetData
from ..commands.signup import SignUp
from ..models.user import NewUserJsonSchema

users_blueprint = Blueprint("users", __name__)


@users_blueprint.get("/users/ping")
def ping():
    return jsonify(Ping().execute())


@users_blueprint.post("/users/reset")
def reset_data():
    reset_data = ResetData()
    reset_data.execute()
    return jsonify({"mssg": "Todos los datos fueron eliminados"}), 200

@users_blueprint.post("/users/signup")
def signup():
    json = request.get_json()
    NewUserJsonSchema.check(json)
    command = SignUp(json.get("email"), json.get("password")).execute()
    return jsonify(command), 201