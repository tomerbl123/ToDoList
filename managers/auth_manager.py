from models.user import User
from run import db

def auth_user(user_name, password):
    password_in_db = db.session.query(User.password).filter_by(user_name=user_name).all()
    if len(password_in_db) != 0:
        password_in_db = password_in_db[0][0]
        if password_in_db == password:
            return True
        else:
            return False
    else:
        return False