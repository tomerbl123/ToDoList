from flask import Flask, request, render_template
from dbupdates import *

app=Flask('__name__')

@app.route('/homepage')
def hello():
	return("hello world")

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)