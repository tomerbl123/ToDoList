from models.user import User
from run import db

def create_user(name, username, password):
	"""
	This function takes the credentials given from the Register page and creates a user entry in the DB.
	:param name: The name of the user.
	:param username: The username of the user.
	:param password: the password of the user.
	"""

	pw_hash = User.set_password(password)

	new_user = User(name, username, pw_hash)
	db.session.add(new_user)
	db.session.commit()