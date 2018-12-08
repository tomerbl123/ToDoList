from flaskapp import *

def addtask(classname,task,isdone='0'):
	NewTask = classname(task, isdone)
	db.session.add(NewTask)
	db.session.commit()

def removetask(classname, taskid):
	q = db.session.query(classname).filter_by(id=taskid)
	q.delete()
	db.session.commit()

def updatetask(classname, taskid, newtask):
	q = db.session.query(classname).filter_by(id=taskid)
	q.update({classname.task: newtask})
	db.session.commit()

#addtask(TasksList,'asd','1')
#removetask(TasksList, 1)
#updatetask(TasksList, 2, 'asdasd')