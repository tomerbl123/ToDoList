from models.task import Task
from run import db

def insert_into_db(task_description_to_insert, task_status_to_insert, the_current_user):
    """
    This function inserts new tasks into the DB.
    """
    if task_status_to_insert == 'yes':
        task_status_to_insert = '1'
    else:
        task_status_to_insert = '0'
    new_task = Task(task_description_to_insert, task_status_to_insert, the_current_user)
    db.session.add(new_task)
    db.session.commit()


def remove_task_from_db(task_to_remove):
    """
    This function removes tasks from the DB, by ID.
    """
    get_task_to_remove = db.session.query(Task.id).filter_by(id=task_to_remove)
    get_task_to_remove.delete()
    db.session.commit()


def edit_task(task_to_edit, task_status_to_insert, new_task_description=None):
    """
    This function updates either the task's ID, Description or both.
    """
    if task_status_to_insert == 'yes':
        task_status_to_insert = '1'
    else:
        task_status_to_insert = '0'

    get_task_to_edit = db.session.query(Task.id).filter_by(id=task_to_edit)

    if len(new_task_description) == 0:
        get_task_to_edit.update({Task.isdone: task_status_to_insert})
    else:
        get_task_to_edit.update({Task.task: new_task_description, Task.isdone: task_status_to_insert})

    db.session.commit()

def get_incomplete_tasks_list(the_current_user):
    """
	This function returns the incomplete tasks list with their IDs.
	"""

    incomplete_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='0').all()
    incomplete_tasks_list_of_dcts = []
    for item in incomplete_tasks_list_of_tuples:
        incomplete_tasks_list_of_dcts.append({item[0]:item[1]})

    return incomplete_tasks_list_of_dcts

def get_done_tasks_list(the_current_user):
    """
	This function returns the done tasks list with their IDs.
	"""

    done_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='1')
    done_tasks_list = []
    for item in done_tasks_list_of_tuples:
        done_tasks_list.append({item[0]:item[1]})

    return done_tasks_list