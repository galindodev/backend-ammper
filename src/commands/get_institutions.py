from .base_command import BaseCommannd
from ..models.user import User
from ..errors.errors import InvalidCredentialsErrors
from ..utils.http import get_institutions_data

class GetInstitutions(BaseCommannd):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        user = User.query.filter_by(id=self.user_id).first()
        if not user:
            raise InvalidCredentialsErrors("User not found")

        return get_institutions_data()