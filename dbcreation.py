from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class TasksList(Base):
	__tablename__='TasksList'

	id=Column(Integer, primary_key=True)
	task=Column(String(80), nullable=False)

	def __init__(self, task=None):
		self.task=task

engine = create_engine('sqlite:////Users/Tomer Ben-Levi/Projects/ToDoList/example.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()