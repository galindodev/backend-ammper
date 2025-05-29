from  sqlalchemy  import  Column, String
from .model import Model, Base
from marshmallow import Schema, fields, validate, ValidationError
from ..errors.errors import ParamError

class User(Model, Base):
	__tablename__ = 'users'

	username = Column(String, nullable=False, unique=False)
	email = Column(String, nullable=False, unique=True)
	link = Column(String, nullable=False, unique=True)
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