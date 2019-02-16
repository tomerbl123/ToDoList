from run import db, app
from models.user import User
from flask import request, redirect, url_for, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from managers.tasks_manager import get_incomplete_tasks_list, get_done_tasks_list
from controllers.auth_controller import auth_controller
from controllers.user_controller import user_controller
from controllers.task_controller import task_controller

login = LoginManager(app)
login.init_app(app)

app.register_blueprint(task_controller)
app.register_blueprint(user_controller)
app.register_blueprint(auth_controller)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
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
def homepage():
	the_current_user = current_user.id

	incomplete_tasks = get_incomplete_tasks_list(the_current_user)
	done_tasks = get_done_tasks_list(the_current_user)

	return render_template('homepage.html', done_tasks = done_tasks, incomplete_tasks = incomplete_tasks)


if __name__ == '__main__':
	print("Running App Locally, about to create DB tables.")
	db.create_all()
	app.run()