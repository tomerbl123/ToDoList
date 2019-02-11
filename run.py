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

#'postgres://ienoldtxeklqyu:6791e4f04297cc8862dfd31697be0505bf64d8b64c6747ae17b69c149613a6b5@ec2-79-125-4-96.eu-west-1.compute.amazonaws.com:5432/dagofqd7saj392',


db=SQLAlchemy(app)
