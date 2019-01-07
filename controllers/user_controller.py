from run import app
from managers import users_manger
from flask import request, redirect, url_for, render_template_string, render_template, Blueprint

user_controller = Blueprint('user_controller', __name__)

@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/new_user', methods=['POST'])
def create_new_user():
	name = request.form.get('name')
	new_user = request.form.get('user_name')
	password = request.form.get('password')

	users_manger.create_user(name, new_user, password)

	return redirect(url_for('login'))