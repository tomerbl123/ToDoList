from __init__ import app, db

class User(db.Model):
	"""
	The users of the system.
	"""
	__tablename__ = 'User'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	user_name = db.Column(db.String, nullable = False)
	password = db.Column(db.String, nullable = False)

	#db.relationship("Tasks")

	def __init__(self, name=None, user_name=None, password=None):
		self.name=name
		self.user_name=user_name
		self.password=password

class Tasks(db.Model):
	"""
	This class creates the Tasks table in the DB.
	There are 3 clomuns here: Task_ID(id), Task_Description(task) and a mark whether the task is done or not (isdone).
	"""
	__tablename__ = 'Tasks'

	id = db.Column(db.Integer, primary_key = True)
	task = db.Column(db.String(255), nullable = False)
	isdone = db.Column(db.String(1), nullable = True)
	#tasks_per_user = db.Column(db.Integer, db.ForeignKey('User.id'))

	def __init__(self, task=None, isdone='0'):
		self.task=task
		self.isdone=isdone
		#self.tasks_per_user=tasks_per_user
	
	def __repr__(self):
		return 'The id is {}, Task is {}'.format(self.id, self.task)
