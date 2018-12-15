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
	__tablename__ = 'AllTasks'

	id=db.Column(db.Integer, primary_key=True)
	task=db.Column(db.String(255), nullable=False)
	isdone=db.Column(db.String(1), nullable=True)

	def __init__(self, task=None, isdone='0'):
		self.task=task
		self.isdone=isdone
	
	def __repr__(self):
		return 'The id is {}, Task is {}'.format(self.id, self.task)

@app.route('/homepage')
@app.route('/homepage/<name>')
def home():
	return render_template('homepage.html')

@app.route('/creating', methods=['POST'])
def createtask(class_name=TasksList):
	query_task = request.form['task']
	NewTask = class_name(query_task)
	db.session.add(NewTask)
	db.session.commit()
	return render_template('homepage.html')

@app.route('/removing', methods=['DELETE'])
def removetask(class_name=TasksList):
	task_id = request.args.get('task_id')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.delete()
	db.session.commit()
	return 'Great Success'

@app.route('/updating', methods=['PATCH'])
def updatetask(class_name=TasksList):
	task_id = request.args.get('task_id')
	new_task = request.args.get('new_task')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.update({class_name.task: new_task})
	db.session.commit()
	return 'Great Success'

@app.route('/gettingall', methods=['GET'])
def getalltasks(class_name=TasksList):
	q = db.session.query(class_name.task, class_name.isdone).all()
	print(q)
	return 'Great Success'

if __name__=='__main__':
	db.create_all()
	app.run(debug=True, use_reloader=False)