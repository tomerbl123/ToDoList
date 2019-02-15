from run import app
from flask import Blueprint, request, redirect, url_for
from flask_login import login_user
from managers import auth_manager
from models.user import User

auth_controller = Blueprint('auth_controller', __name__)


@app.route('/auth', methods=['GET', 'POST'])
def auth_user():
    user_name = request.form.get('user_name')
    password = request.form.get('password')

    result = auth_manager.auth_user(user_name, password)
    user = User.query.filter_by(user_name=user_name).first()

    if result:
        login_user(user)
        print('Successful login for {}'.format(user))
        return redirect(url_for('homepage'))
    else:
        print('Wrong Username or Password for user {}'.format(user))
        return redirect(url_for('login'))