from .base_command import BaseCommannd
from models.db import db
from models.user import User
from utils.http import create_link_user
from errors.errors import DuplicatedUserError
import re

class SignUp(BaseCommannd):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.username = re.sub(r'\d+', '', self.email.replace('@', '').replace('.', ''))

    def execute(self):
        self.exist_user()
        self.link_id = create_link_user(self.username, self.password)

        user = User(
            username=self.username,
            email=self.email,
            link=self.link_id,
            password=self.password
        )
        db.session.add(user)
        db.session.commit()

        return {
            "mssg": "User created successfully",
            "user": {
                "username": self.username,
                "email": self.email,
                "link": self.link_id
            }
        }
    
    def exist_user(self):
        user = User.query.filter_by(email=self.email).first()
        if user:
            raise DuplicatedUserError()