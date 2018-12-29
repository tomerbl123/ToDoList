def creating_table_rows_string(data_base, class_name):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""

	#Querying the amount of tasks that we have (done and not done).
	amount_of_not_done_tasks = data_base.session.query(class_name.id, class_name.task, class_name.isdone).filter_by(isdone='0').count()
	amount_if_done_tasks = data_base.session.query(class_name.id, class_name.task, class_name.isdone).filter_by(isdone='1').count()
	
	done_tasks_list=[]
	not_done_tasks_list=[]
	html_changing_part = ''

	#Creating the NOT Done tasks' table (no tasks -> no table).
	if amount_of_not_done_tasks > 0:
		data_not_done = data_base.session.query(class_name.id, class_name.task, class_name.isdone).filter_by(isdone='0')
		not_done_tasks_list.append("""<h2>What should I do?</h2><table style="width:100%"><tr><th>Number</th><th>Description</th></tr>""")
		for item in data_not_done:
			text = "<tr><td>{0}</td><td>{1}</td></tr>".format(item[0], item[1])
			not_done_tasks_list.append(text)
		not_done_tasks_list.append("""</table><br><br>""")
	else:
		not_done_tasks_list.append("""<h2>Nothing to do...</h2><br>""")

	#Creating the Done tasks' table (no tasks -> no table).
	if amount_if_done_tasks > 0:
		data_done = data_base.session.query(class_name.id, class_name.task, class_name.isdone).filter_by(isdone='1')
		done_tasks_list.append("""<h2>Done Tasks:</h2><table style="width:100%"><tr><th>Number</th><th>Description</th></tr>""")
		for item in data_done:
			text = "<tr><td>{0}</td><td>{1}</td></tr>".format(item[0], item[1])
			done_tasks_list.append(text)
		done_tasks_list.append("""</table>""")

	#Creating the unified tasks (Done and NOT Done string).
	for item in not_done_tasks_list:
		html_changing_part += item

	for item in done_tasks_list:
		html_changing_part += item

	return html_changing_part

def create_and_return_full_html_string(data_base, class_name):
	"""
	This fuction takes all the parts of the HTML String and combine them into one FULL HTML String.
	"""
	closer="""</body></html>"""

	with open('C:/Users/Tomer Ben-Levi/Projects/ToDoList/templates/homepage.html', "r") as f:
		text = f.read()

	html_changing_part = creating_table_rows_string(data_base, class_name)
	full_html = str(text) + html_changing_part + closer
	
	return full_html

def insert_into_db(data_base, class_name, task_description_to_insert, task_status_to_insert):
	"""
	This function inserts new tasks into the DB.
	"""
	if task_status_to_insert == 'yes':
		task_status_to_insert = '1'
	else:
		task_status_to_insert = '0'
	NewTask = class_name(task_description_to_insert, task_status_to_insert)
	data_base.session.add(NewTask)
	data_base.session.commit()

def remove_task_from_db(data_base, class_name, task_to_remove):
	"""
	This function removes tasks from the DB, by ID.
	"""
	get_task_to_remove = data_base.session.query(class_name.id).filter_by(id=task_to_remove)
	get_task_to_remove.delete()
	data_base.session.commit()

def edit_task(data_base, class_name, task_to_edit, task_status_to_insert, new_task_description=None):
	"""
	This function updates either the task's ID, Description or both.
	"""
	if task_status_to_insert == 'yes':
		task_status_to_insert = '1'
	else:
		task_status_to_insert = '0'

	get_task_to_edit = data_base.session.query(class_name.id).filter_by(id=task_to_edit)
	
	if len(new_task_description) == 0:
		get_task_to_edit.update({class_name.isdone: task_status_to_insert})
	else:	
		get_task_to_edit.update({class_name.task: new_task_description, class_name.isdone: task_status_to_insert})
	
	data_base.session.commit()

def create_user(data_base, class_name, name, user_name, password):
	New_User = class_name(name, user_name, password)
	data_base.session.add(New_User)
	data_base.session.commit()

def auth(data_base, class_name, user_name, password):
	password_in_db = data_base.session.query(class_name.password).filter_by(user_name = user_name).all()
	password_in_db = password_in_db[0][0]
	if password_in_db == password:
		return 'Yes'
	else:
		return 'No'