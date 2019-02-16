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

	def __init__(self, name, user_name, password):
		self.name = name
		self.user_name = user_name
		self.password = password

	@staticmethod
	def set_password(password):
		return generate_password_hash(password)

	@staticmethod
	def check_password(restored_password, login_given_password):
		return check_password_hash(restored_password, login_given_password)