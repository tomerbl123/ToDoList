from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('__name__')

app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI='sqlite:////Users/Tomer Ben-Levi/Projects/ToDoList/example.db',
	SQLALCHEMY_TRACK_MODIFICATIONS=False)

db=SQLAlchemy(app)