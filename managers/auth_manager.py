from models.user import User
from run import db

def auth_user(user_name, login_password):
    """
    This function makes authentication using a given password and username.
    :param user_name: The user that we want to authenticate.
    :param login_password: The password that we need to check the hash of it and compare it to the hashed password
    in the DB.
    """

    get_password_from_db = db.session.query(User.password).filter_by(user_name=user_name).all()
    password_from_db = [password for (password, ) in get_password_from_db]

    try:
        return User.check_password(password_from_db[0], login_password)
    except IndexError:
        print("After trying to fetch the password from the DB, no value found.")