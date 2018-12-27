from __init__ import app, db
from models import Tasks
from flask import request, redirect, url_for, render_template_string
from controllers import insert_into_db, create_and_return_full_html_string, remove_task_from_db, edit_task

@app.route('/homepage', methods=['GET'])
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
	app.run(debug=True, use_reloader=False)