from run import db, app
from models.task import Task
from models.user import User
from flask import request, redirect, url_for, render_template_string, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from controllers.task_controller import task_controller
from controllers.user_controller import user_controller
from controllers.auth_controller import auth_controller

login = LoginManager(app)
login.init_app(app)

app.register_blueprint(task_controller, '/task')
app.register_blueprint(user_controller, '/user')
app.register_blueprint(auth_controller, '/auth')


@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/homepage', methods=['GET'])
@login_required
def homepage(data_base = db, class_name = Task):
	the_current_user = current_user.id
	full_html = create_and_return_full_html_string(data_base, class_name, the_current_user)
	return render_template_string(full_html)


if __name__=='__main__':
	db.create_all()
	app.run()