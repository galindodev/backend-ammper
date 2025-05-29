from  sqlalchemy  import  Column, String
from .model import Model, Base


class User(Model, Base):
	__tablename__ = 'users'

	username = Column(String, nullable=False, unique=True)
	email = Column(String, nullable=False, unique=True)
	link = Column(String, nullable=False, unique=True)
	password = Column(String, nullable=False)

