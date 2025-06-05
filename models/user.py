from sqlalchemy  import  Column, String
from .model import Model, Base
from marshmallow import Schema, fields, validate, ValidationError
from errors.errors import ParamError, InvalidCredentialsErrors, MissingAuthParams

class User(Model, Base):
	__tablename__ = 'users'
	email = Column(String, nullable=False, unique=True)
	password = Column(String, nullable=False)

class NewUserJsonSchema(Schema):
    password = fields.String(required=True, validate=validate.Length(min=1, max=255))
    email = fields.Email(required=True, validate=validate.Length(max=255))

    @staticmethod
    def check(json):
        try:
            NewUserJsonSchema().load(json)
        except ValidationError as exception:
            raise ParamError.first_from(exception.messages)
        

class AuthUserJsonSchema(Schema):
    email = fields.String(validate=validate.Length(min=1, max=255))
    password = fields.String(validate=validate.Length(min=1, max=255))

    @staticmethod
    def check(json):
        AuthUserJsonSchema.check_empty(json)
        try:
            AuthUserJsonSchema().load(json)
        except ValidationError:
            raise InvalidCredentialsErrors()

    @staticmethod
    def check_empty(json):
        fields = ['email', 'password']
        if not any(field in json for field in fields):
            raise MissingAuthParams()
        for field in fields:
            if field not in json or not json[field]:
                raise MissingAuthParams()