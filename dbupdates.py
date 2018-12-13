from flaskapp import TasksList, db

def addtask(class_name, task, is_done='0'):
	NewTask = class_name(task, is_done)
	db.session.add(NewTask)
	db.session.commit()

def removetask(class_name, task_id):
	q = db.session.query(class_name).filter_by(id=task_id)
	q.delete()
	db.session.commit()

def updatetask(class_name, task_id, newtask):
	q = db.session.query(class_name).filter_by(id=task_id)
	q.update({class_name.task: newtask})
	db.session.commit()

def getalltasks(class_name):
	q = db.session.query(class_name.task).all()
	print(q)


#addtask(TasksList,'asd','1')
#removetask(TasksList, 1)
#updatetask(TasksList, 2, 'asdasd')
#getalltasks(TasksList)