from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..commands.get_accounts import GetAccounts
from ..commands.get_institutions import GetInstitutions
from ..commands.get_transation import GetTransactions
from ..models.belvos import IdAccountSchema


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

@belvos_blueprint.post("/belvos/transactions")
@jwt_required()
def get_transactions():
    json = request.get_json()
    IdAccountSchema.check(json)
    user_id = get_jwt_identity()  
    command = GetTransactions(user_id, json["account_id"]).execute()
    return jsonify(command), 200