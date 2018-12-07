from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
#import dbcreation
from dbcreation import TasksList, session

app=Flask('__name__')

@app.route('/homepage')
def hello():
	return("hello world")

def addtasktodb(task):
	NewTask = TasksList(task)
	session.add(NewTask)
	session.commit()
	#why it adds the items twice?? what the TasksList class really does?
addtasktodb('something')

if __name__=='__main__':
    app.run(debug=True)