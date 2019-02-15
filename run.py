from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('__name__')

app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI='sqlite:////ToDoList/Tasks.db',
	SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG = True,
	use_reloader=False)

db=SQLAlchemy(app)
db.create_all()