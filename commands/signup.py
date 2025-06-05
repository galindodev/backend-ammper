from .base_command import BaseCommannd
from models.db import db
from models.user import User
from errors.errors import DuplicatedUserError
import re

class SignUp(BaseCommannd):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def execute(self):
        self.exist_user()
        user = User(
            email=self.email,
            password=self.password
        )
        db.session.add(user)
        db.session.commit()

        return {
            "mssg": "User created successfully",
            "user": {
                "email": self.email,
            }
        }
    
    def exist_user(self):
        user = User.query.filter_by(email=self.email).first()
        if user:
            raise DuplicatedUserError()