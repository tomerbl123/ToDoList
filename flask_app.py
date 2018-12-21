from __init__ import app, db
from models import Tasks
from flask import request, redirect, url_for, render_template_string
from controllers import insert_into_db, return_full_html

@app.route('/homepage', methods=['GET'])
def homepage(data_base = db, class_name = Tasks):
	full_html = return_full_html(data_base, class_name)
	return render_template_string(full_html)

@app.route('/creating', methods=['POST'])
def create_task(data_base = db, class_name = Tasks):
	task_to_insert = request.form['task']
	insert_into_db(db, task_to_insert, class_name)
	return redirect(url_for('homepage'))

@app.route('/removing', methods=['DELETE'])
def remove_task(class_name=Tasks):
	task_id = request.args.get('task_id')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.delete()
	db.session.commit()
	return 'Great Success'

@app.route('/updating', methods=['PATCH'])
def update_task(class_name=Tasks):
	task_id = request.args.get('task_id')
	new_task = request.args.get('new_task')
	q = db.session.query(class_name).filter_by(id=task_id)
	q.update({class_name.task: new_task})
	db.session.commit()
	return 'Great Success'

if __name__=='__main__':
	db.create_all()
	app.run(debug=True, use_reloader=False)

"""
WHAT'S NEXT:
- Add the Remove and Update options - text field with task number maybe.
- Use Git.
"""