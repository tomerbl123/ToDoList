from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import dbcreation
from dbcreation import TasksList, session

app=Flask('__name__')

@app.route('/homepage')
def hello():
	return("hello world")

NewTask = TasksList('tomer')
session.add(NewTask)
session.commit()

if __name__=='__main__':
    app.run(debug=True)