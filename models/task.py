from run import db
from flask_login import UserMixin

class Task(db.Model):
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