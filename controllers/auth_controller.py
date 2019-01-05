from flask import Blueprint
from managers import auth_manager
auth_controller = Blueprint('auth_controller', __name__)


@app.route('/auth', methods=['GET', 'POST'])
def auth_user():
	user_name = request.form.get('user_name')
	password = request.form.get('password')

    result = auth_manager.auth_user(user_name, password)

    if result:
        login_user(user)
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('login'))