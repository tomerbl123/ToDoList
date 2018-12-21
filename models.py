from __init__ import app, db

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