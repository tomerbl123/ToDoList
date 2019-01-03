from run import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
	"""
	The users of the system.
	"""
	__tablename__ = 'User'

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	name = db.Column(db.String(30), nullable = False)
	user_name = db.Column(db.String(64), nullable = False, unique=True)
	password = db.Column(db.String(128), nullable = False)

	db.relationship("Tasks")

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

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	task = db.Column(db.String(255), nullable = False)
	isdone = db.Column(db.String(1), nullable = True)

	user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

	def __init__(self, task=None, isdone='0', user_id=None):
		self.task=task
		self.isdone=isdone
		self.user_id=user_id