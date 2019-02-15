from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask('__name__')

app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
	SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG = True,
	use_reloader=False)

db=SQLAlchemy(app)
db.create_all()
