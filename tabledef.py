from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

####################

class User(Base):
	""""""
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)

	#--------------
	def __init__(self, username, password):
		""""""
		self.username = username
		self.password = password

class Event(Base):
	""""""
	__tablename__ = "events"

	id = Column(Integer, primary_key=True)
	user = Column(String)
	notes = Column(String)
	created = Column(DateTime, default=datetime.datetime.utcnow)

	#--------------
	def __init__(self, username, notes):
		""""""
		self.user = username
		self.notes = notes
		self.created = datetime.utcnow()

# Create tables
Base.metadata.create_all(engine)
