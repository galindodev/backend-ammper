from .base_command import BaseCommannd
from ..models.db import db
from ..models.user import User


class ResetData(BaseCommannd):
    def execute(self):
        User.query.delete()
        db.session.commit()
