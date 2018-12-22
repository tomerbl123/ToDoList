def static_html_string():
	"""
	This function defines the static part of the HTML string and return it.
	"""
	html_static_part = """
	<!DOCTYPE html>
	<html>
		<head>
			<title>ToDoList</title>

			<style>
		        body {
				  background-color: lightgray;
				}
		        table {
		            font-family: arial, sans-serif;
		            border-collapse: collapse;
		        }
		        td, th {
		            border: 1px solid #dddddd;
		            text-align: left;
		            padding: 5px;
		        }
		      	th.id {
		      		padding: 5px;
		      		width: 10%;
		      	}
		        tr:nth-child(even) {
		            background-color: #dddddd;
		        }
        	</style>
		</head>
		<body>
			<h1>Welcome to your ToDoList app</h1>
			
			<form action="creating" method="post">
				<fieldset>
					<legend><strong>Adding New Task</strong></legend>
					<div>
					Description:

					<br>

					<textarea rows="3" cols="40" name="task"></textarea>

					<br>
					
					<input type="checkbox" name="is_done" value="yes"> Mark as Done
					</div>
					
					<br>

					<input type="submit" value="Save changes">
					<input type="reset" value="Discard changes" id="hello">
				</fieldset>
			</form>
				
				<br>

			<form action="updating" method="post">
				<fieldset>
					<legend><strong>Editing a Task</strong></legend>
					<div>
					Task's Number(limited to one): 

					<br>
					
					<input type="text" name="task_id">

					<br>
					Description:

					<br>

					<textarea rows="3" cols="40" name="new_task"></textarea>
					
					<br>

					<input type="checkbox" name="is_done" value="yes"> Mark as Done
					</div>

					<br>

					<input type="submit" value="Save changes">
					<input type="reset" value="Discard changes">
				</fieldset>
			</form>
				
				<br>

			<form action="removing" method="post">
				<fieldset>
					<legend><strong>Deleting a Task</strong></legend>
					<div>
					Task's Number(limited to one): 
					
					<br>

					<input type="text" name="task_id">
					</div>
				

				<br>

				<input type="submit" value="Save changes">
				<input type="reset" value="Discard changes">
				</fieldset>
			</form>

			<br><br>
	"""
	return html_static_part
				  
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

def create_full_html_string(html_static_part, html_changing_part):
	"""
	This fuction takes all the parts of the HTML String and combine them into one FULL HTML String.
	"""
	closer="""</body></html>"""
	full_html = html_static_part + html_changing_part + closer
	return full_html

def return_full_html(data_base, class_name):
	"""
	This function returns the full HTML String.
	The purpose here is to be able to call just one function when we want to render 
	the	Homepage's HTML String (instead of 3 functions)
	"""
	html_static_part = static_html_string()
	html_changing_part = creating_table_rows_string(data_base, class_name)
	full_html = create_full_html_string(html_static_part, html_changing_part)
	return full_html

def get_all_tasks(data_base, class_name):
	"""
	This function querying all the taks from Tasks table.
	"""
	get_all_tasks_query = data_base.session.query(class_name.id, class_name.isdone, class_name.task).all()
	return(get_all_tasks_query)

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