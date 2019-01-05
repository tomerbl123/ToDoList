from flask import Blueprint
from flask import request, redirect, url_for, render_template_string, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

task_controller = Blueprint('task_controller', __name__)

@app.route('/creating', methods=['POST'])
@login_required
def create_task():
	task_description_to_insert = request.form.get('task')
	task_status_to_insert = request.form.get('is_done')

	the_current_user = current_user.id

	insert_into_db(task_description_to_insert, task_status_to_insert, the_current_user)
	return redirect(url_for('homepage'))

@app.route('/updating', methods=['POST'])
@login_required
def update_task():
	task_id = request.form.get('task_id')
	new_task = request.form.get('new_task')
	is_done = request.form.get('is_done')
	edit_task(task_id, is_done, new_task,)
	return redirect(url_for('homepage'))

@app.route('/removing', methods=['POST'])
@login_required
def remove_task():
	task_id = request.form.get('task_id')
	remove_task_from_db(task_id)
	return redirect(url_for('homepage'))