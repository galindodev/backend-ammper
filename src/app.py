from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv('.env.development')

from .blueprints.users import users_blueprint
from .errors.errors import ApiError
from .models.db import init_db
import os

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)
init_db(app)

app.register_blueprint(users_blueprint)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        'mssg': err.description
    }
    return jsonify(response), err.code