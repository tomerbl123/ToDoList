from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class TasksList(Base):
	__tablename__='alltasks'

	id=Column(Integer, primary_key=True)
	task=Column(String(255), nullable=False)
	isdone=Column(String(1), nullable=False)

	def __init__(self, task=None, isdone='0'):
		self.task=task
		self.isdone=isdone

	def __repr__(self):
		return 'The Task is {}'.format(self.task)

engine = create_engine('sqlite:////Users/Tomer Ben-Levi/Projects/ToDoList/example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()