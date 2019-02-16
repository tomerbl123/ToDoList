from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask('__name__')

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
	app.config.update(
		SECRET_KEY='topsecret',
		SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		DEBUG = True,
		use_reloader=False)
else:
	app.config.update(
		SECRET_KEY='topsecret',
		SQLALCHEMY_DATABASE_URI='sqlite:////ToDoList/Tasks.db',
		SQLALCHEMY_TRACK_MODIFICATIONS=False,
		DEBUG = True,
		use_reloader=False)

db=SQLAlchemy(app)
db.create_all()