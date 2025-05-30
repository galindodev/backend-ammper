from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..commands.get_accounts import GetAccounts
from ..commands.get_institutions import GetInstitutions



belvos_blueprint = Blueprint("belvos", __name__)

@belvos_blueprint.get("/belvos/institutions")
@jwt_required()  
def get_institutions():
    user_id = get_jwt_identity()  
    command = GetInstitutions(user_id).execute()
    return jsonify(command), 200

@belvos_blueprint.get("/belvos/accounts")
@jwt_required()
def get_accounts():
    user_id = get_jwt_identity()  
    command = GetAccounts(user_id).execute()
    return jsonify(command), 200