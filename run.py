from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('__name__')

app.config.update(
	SECRET_KEY='topsecret',
	SQLALCHEMY_DATABASE_URI='postgres://ddbkzqemmhbsfe:473523aa042702f7e7b6e763df7e59600a7f4dcdfd4ea2280b075f6bc61d7939@ec2-54-217-208-105.eu-west-1.compute.amazonaws.com:5432/danqr65is0894t',
	SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG = True,
	use_reloader=False)

db=SQLAlchemy(app)