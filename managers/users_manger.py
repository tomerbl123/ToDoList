from models.user import User
from run import db

def create_user(name, user_name, password):
	New_User = User(name, user_name, password)
	db.session.add(New_User)
	db.session.commit()