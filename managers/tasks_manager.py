from models.task import Task
from run import db

def add_task_to_db(task_description_to_insert, the_current_user):
    """
    Here we add task entry to the DB.
    The default tasks status is Incomplete (0).
    :param task_description_to_insert: The tasks content.
    :param the_current_user: The user that we want to "attach" the task to.
    """

    new_task = Task(task=task_description_to_insert, user_id=the_current_user)
    db.session.add(new_task)
    db.session.commit()


def remove_task_from_db(task_to_remove):
    """
    Removes a task entry from the DB.
    :param task_to_remove: The task's ID.
    """

    get_task_to_remove = db.session.query(Task.id).filter_by(id=task_to_remove)
    get_task_to_remove.delete()
    db.session.commit()


def edit_task(task_to_edit, task_status_to_insert, new_task_description):
    """
    Edits a task.
    :param task_to_edit: The task's ID.
    :param task_status_to_insert: The new status to insert.
    :param new_task_description: The new content to insert.
    """

    if task_status_to_insert:
        task_status_to_insert = '1'
    else:
        task_status_to_insert = '0'

    get_task_to_edit = db.session.query(Task.id).filter_by(id=task_to_edit)

    if new_task_description:
        get_task_to_edit.update({Task.task: new_task_description, Task.isdone: task_status_to_insert})
    else:
        get_task_to_edit.update({Task.isdone: task_status_to_insert})

    db.session.commit()

def get_incomplete_tasks_list(the_current_user):
    """

    :param the_current_user:
    :return:
    """

    incomplete_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='0').all()
    incomplete_tasks_list_of_dicts = []
    for item in incomplete_tasks_list_of_tuples:
        incomplete_tasks_list_of_dicts.append({item[0]:item[1]})

    return incomplete_tasks_list_of_dicts

def get_done_tasks_list(the_current_user):
    """

    :param the_current_user:
    :return:
    """

    done_tasks_list_of_tuples = db.session.query(Task.id, Task.task).filter_by(user_id=the_current_user, isdone='1')
    done_tasks_list = []
    for item in done_tasks_list_of_tuples:
        done_tasks_list.append({item[0]:item[1]})

    return done_tasks_list