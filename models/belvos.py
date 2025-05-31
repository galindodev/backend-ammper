from marshmallow import Schema, fields, validate, ValidationError
from errors.errors import InvalidCredentialsErrors, MissingAuthParams


class IdAccountSchema(Schema):
    account_id = fields.String(required=True, validate=validate.Length(min=1, max=255))

    @staticmethod
    def check(json):
        IdAccountSchema.check_empty(json)
        try:
            IdAccountSchema().load(json)
        except ValidationError:
            raise InvalidCredentialsErrors()

    @staticmethod
    def check_empty(json):
        fields = ['account_id']
        if not any(field in json for field in fields):
            raise MissingAuthParams()
        for field in fields:
            if field not in json or not json[field]:
                raise MissingAuthParams()
            
class AccountsSchema(Schema):
    bank_name = fields.String(required=True, validate=validate.Length(min=1, max=255))

    @staticmethod
    def check(json):
        AccountsSchema.check_empty(json)
        try:
            AccountsSchema().load(json)
        except ValidationError:
            raise InvalidCredentialsErrors()

    @staticmethod
    def check_empty(json):
        fields = ['bank_name']
        if not any(field in json for field in fields):
            raise MissingAuthParams()
        for field in fields:
            if field not in json or not json[field]:
                raise MissingAuthParams()