from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
#from dbupdates import *

app=Flask('__name__')

#Changing some basic configurations in the Application.
app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI='sqlite:////Users/Tomer Ben-Levi/Projects/ToDoList/example.db',
	SQLALCHEMY_TRACK_MODIFICATIONS=False)

db=SQLAlchemy(app)

class TasksList(db.Model):
	"""
	This class creates the TasksList table in the DB.
	There are 3 clomuns here: Task_ID(id), Task_Description(task) and a mark whether the task is done or not (isdone).
	"""
	__tablename__ = 'ihatemylife'

	id=db.Column(db.Integer, primary_key=True)
	task=db.Column(db.String(255), nullable=False)
	isdone=db.Column(db.String(1), nullable=True)

	def __init__(self, task=None, isdone='0'):
		self.task=task
		self.isdone=isdone
	
	def __repr__(self):
		return 'The id is {}, Task is {}'.format(self.id, self.task)

@app.route('/homepage')
def hello():
	return("hello world")

if __name__=='__main__':
	db.create_all()
	app.run(debug=True, use_reloader=False)