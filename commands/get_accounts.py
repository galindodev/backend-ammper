from .base_command import BaseCommannd
from models.user import User
from errors.errors import InvalidCredentialsErrors
from utils.http import get_accounts_data



class GetAccounts(BaseCommannd):
    def __init__(self, user_id, bank_name):
        self.user_id = user_id
        self.bank_name = bank_name

    def execute(self):
        user = User.query.filter_by(id=self.user_id).first()
        if not user:
            raise InvalidCredentialsErrors()
        data_account = get_accounts_data()['results']

        list_banks = []
        for element in data_account:
            if element['institution']['name'] == self.bank_name:
                list_banks.append({
                    'account_id': element['id'],
                    'bank_name': element['institution']['name'],
                    'link_id': element['link'],
                    'name': element['name'],
                    'type': element['type'],
                    'balance': element['balance']['current'],
                    'available': element['balance']['available'],
                    'number': element['number'],
                })

        return list_banks 