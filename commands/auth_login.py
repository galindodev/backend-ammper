from .base_command import BaseCommannd
from models.user import User
from errors.errors import InvalidCredentialsErrors
from flask_jwt_extended import create_access_token
from datetime import timedelta

class Login(BaseCommannd):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def execute(self):
        user = User.query.filter_by(email=self.email).first()
        if not user or user.password != self.password:
            raise InvalidCredentialsErrors()
        
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                "email": user.email
            },
            expires_delta=timedelta(minutes=20)
        )

        return {
            "token": access_token,
            "user": {
                "email": user.email,
            }
        }