from flask import Flask, request, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from controllers import static_html_rendering

app=Flask('__name__')
#Changing some basic configurations in the Application.
app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI='sqlite:////Users/Tomer Ben-Levi/Projects/ToDoList/example.db',
	SQLALCHEMY_TRACK_MODIFICATIONS=False)

db=SQLAlchemy(app)

class Tasks(db.Model):
	"""
	This class creates the Tasks table in the DB.
	There are 3 clomuns here: Task_ID(id), Task_Description(task) and a mark whether the task is done or not (isdone).
	"""
	__tablename__ = 'Tasks'

	id=db.Column(db.Integer, primary_key=True)
	task=db.Column(db.String(255), nullable=False)
	isdone=db.Column(db.String(1), nullable=True)

	def __init__(self, task=None, isdone='0'):
		self.task=task
		self.isdone=isdone
	
	def __repr__(self):
		return 'The id is {}, Task is {}'.format(self.id, self.task)

@app.route('/homepage', methods=['GET'])
def homepage():
	html_structure = static_html_rendering()
	return render_template_string(html_structure)

@app.route('/creating', methods=['POST'])
def create_task(class_name=Tasks):
	query_task = request.form['task']
	NewTask = class_name(query_task)
	db.session.add(NewTask)
	db.session.commit()
	return render_template('homepage.html')

@app.route('/removing', methods=['DELETE'])
def remove_task(class_name=Tasks):
	task_id = request.args.get('task_id')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.delete()
	db.session.commit()
	return 'Great Success'

@app.route('/updating', methods=['PATCH'])
def update_task(class_name=Tasks):
	task_id = request.args.get('task_id')
	new_task = request.args.get('new_task')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.update({class_name.task: new_task})
	db.session.commit()
	return 'Great Success'
	
if __name__=='__main__':
	db.create_all()
	app.run(debug=True, use_reloader=False)