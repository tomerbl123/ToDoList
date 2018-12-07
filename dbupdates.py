from dbcreation import TasksList, session

def addtask(classname,task,isdone='0'):
	NewTask = classname(task, isdone)
	session.add(NewTask)
	session.commit()

def removetask(classname, taskid):
	q = session.query(classname).filter_by(id=taskid)
	q.delete()
	session.commit()

def updatetask(classname, taskid, newtask):
	q = session.query(classname).filter_by(id=taskid)
	q.update({classname.task: newtask})
	session.commit()

#addtask(TasksList,'asd','1')
#removetask(TasksList, 1)
#updatetask(TasksList, 2, 'asdasd')