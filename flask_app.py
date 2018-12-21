from __init__ import app, db
from models import Tasks
from flask import request, render_template_string, render_template
from controllers import static_html_string, creating_table_rows_string, create_full_html_string, get_all_tasks

@app.route('/homepage', methods=['GET'])
def homepage():
	html_static_part = static_html_string()
	html_changing_part = creating_table_rows_string(db, Tasks)
	full_html = create_full_html_string(html_static_part, html_changing_part)
	return render_template_string(full_html)

@app.route('/creating', methods=['POST'])
def create_task(class_name=Tasks):
	query_task = request.form['task']
	NewTask = class_name(query_task)
	db.session.add(NewTask)
	db.session.commit()
	return render_template_string(homepage())

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
- Fix the bug with the creating page that opens after adding a task and gets stuck.
- Add the Remove and Update options - text field with task number maybe.
- Use Git.
"""