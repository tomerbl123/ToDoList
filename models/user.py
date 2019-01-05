from run import db
from flask_login import UserMixin

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