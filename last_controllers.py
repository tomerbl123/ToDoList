from run import db
from models.task import Task

def get_done_tasks_list(the_current_user):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""

	done_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='1')
	done_tasks_list = []
	for item in done_tasks_list_of_tuples:
		done_tasks_list.append({item[0]:item[1]})

	#print(done_tasks_list)
	return done_tasks_list

def get_incomplete_tasks_list(the_current_user):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""

	incomplete_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='0').all()
	incomplete_tasks_list_of_dcts = []
	for item in incomplete_tasks_list_of_tuples:
		incomplete_tasks_list_of_dcts.append({item[0]:item[1]})

	#print(incomplete_tasks_list_of_dcts)
	return incomplete_tasks_list_of_dcts

#get_done_tasks_list(1)
#get_incomplete_tasks_list(1)