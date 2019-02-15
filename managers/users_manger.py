from models.user import User
from run import db

def create_user(name, user_name, password):
	new_user = User(name, user_name, password)
	db.session.add(new_user)
	db.session.commit()