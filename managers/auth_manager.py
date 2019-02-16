from models.user import User
from run import db

def auth_user(user_name, password):
    password_in_db = db.session.query(User.password).filter_by(user_name=user_name).all()

    if password_in_db:
        if password_in_db[0][0] == password:
            return True