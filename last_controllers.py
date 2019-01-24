from run import db
from models.task import Task

def creating_table_rows_string(the_current_user):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""

	#Querying the amount of tasks that we have (done and not done).
	amount_of_not_done_tasks = db.session.query(Task.id).filter_by(user_id=the_current_user, isdone='0').count()
	amount_if_done_tasks = db.session.query(Task.id).filter_by(user_id=the_current_user, isdone='1').count()
	
	done_tasks_list=[]
	not_done_tasks_list=[]
	html_changing_part = ''

	#Creating the NOT Done tasks' table (no tasks -> no table).
	if amount_of_not_done_tasks > 0:
		data_not_done = db.session.query(Task.id, Task.task, Task.isdone).filter_by(user_id=the_current_user, isdone='0')
		not_done_tasks_list.append("""<h2>What should I do?</h2><table><tr><th>Number</th><th>Description</th></tr>""")
		for item in data_not_done:
			text = "<tr><td>{0}</td><td>{1}</td></tr>".format(item[0], item[1])
			not_done_tasks_list.append(text)
		not_done_tasks_list.append("""</table>""")
	else:
		not_done_tasks_list.append("""<h2>Nothing to do...</h2>""")

	#Creating the Done tasks' table (no tasks -> no table).
	if amount_if_done_tasks > 0:
		data_done = db.session.query(Task.id, Task.task, Task.isdone).filter_by(user_id=the_current_user, isdone='1')
		done_tasks_list.append("""<h2>Great Success!</h2><table><tr><th>Number</th><th>Description</th></tr>""")
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

def create_and_return_full_html_string(the_current_user):
	"""
	This fuction takes all the parts of the HTML String and combine them into one FULL HTML String.
	"""
	closer="""</body></html>"""

	with open('C:/ToDoList/templates/homepage.html', "r") as f:
		text = f.read()

	html_changing_part = creating_table_rows_string(the_current_user)
	full_html = str(text) + html_changing_part + closer
	
	return full_html