from __init__ import db, app
from models.models import Tasks, User
from flask import request, redirect, url_for, render_template_string, render_template, Response, session, abort
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from controllers import insert_into_db, create_and_return_full_html_string, remove_task_from_db, \
						edit_task, create_user, auth

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login(data_base = db, class_name = User):
	return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth_user(data_base = db, class_name = User):
	user_name = request.form.get('user_name')
	password = request.form.get('password')

	user = User.query.filter_by(user_name=user_name).first()
	success_or_not = auth(data_base, class_name, user_name, password)

	if success_or_not == 'Yes':
		login_user(user)
		return redirect(url_for('homepage'))
	else:
		return redirect(url_for('login'))

@app.route('/register')
def register(data_base = db, class_name = User):
	return render_template('register.html')

@app.route('/new_user', methods=['POST'])
def create_new_user(data_base = db, class_name = User):
	name = request.form.get('name')
	new_user = request.form.get('user_name')
	password = request.form.get('password')
	create_user(data_base, class_name, name, new_user, password)
	return redirect(url_for('login'))

@app.route('/homepage', methods=['GET'])
@login_required
def homepage(data_base = db, class_name = Tasks):
	full_html = create_and_return_full_html_string(data_base, class_name)
	return render_template_string(full_html)

@app.route('/creating', methods=['POST'])
def create_task(data_base = db, class_name = Tasks):
	task_description_to_insert = request.form.get('task')
	task_status_to_insert = request.form.get('is_done')
	insert_into_db(db, class_name, task_description_to_insert, task_status_to_insert)
	return redirect(url_for('homepage'))

@app.route('/removing', methods=['POST'])
def remove_task(data_base = db, class_name = Tasks):
	task_id = request.form.get('task_id')
	remove_task_from_db(data_base, class_name, task_id)
	return redirect(url_for('homepage'))

@app.route('/updating', methods=['POST'])
def update_task(data_base = db, class_name = Tasks):
	task_id = request.form.get('task_id')
	new_task = request.form.get('new_task')
	is_done = request.form.get('is_done')
	edit_task(data_base, class_name, task_id, is_done, new_task,)
	return redirect(url_for('homepage'))

if __name__=='__main__':
	db.create_all()
	app.run()