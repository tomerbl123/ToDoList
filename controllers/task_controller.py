from run import app
from managers import tasks_manager
from flask import request, redirect, url_for, Blueprint
from flask_login import login_required, current_user

task_controller = Blueprint('task_controller', __name__)

@app.route('/creating', methods=['POST'])
@login_required
def create_task():
	task_description_to_insert = request.form.get('task')

	the_current_user = current_user.id

	tasks_manager.add_task_to_db(task_description_to_insert, the_current_user)

	print("Successfully added task for user: {}".format(current_user.id))

	return redirect(url_for('homepage'))

@app.route('/updating', methods=['POST'])
@login_required
def update_task():
	task_id = request.form.get('task_id')
	new_task = request.form.get('new_task')
	is_done = request.form.get('is_done')

	tasks_manager.edit_task(task_id, is_done, new_task)

	print("Edited task successfully")

	return redirect(url_for('homepage'))

@app.route('/removing', methods=['POST'])
@login_required
def remove_task():
	task_id = request.form.get('task_id')
	tasks_manager.remove_task_from_db(task_id)

	print("Deleted task successfully")

	return redirect(url_for('homepage'))