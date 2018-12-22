def static_html_string():
	"""
	This function defines the static part of the HTML string and return it.
	"""
	html_static_part = """
	<!DOCTYPE html>
	<html>
		<head>
			<title>ToDoList</title>

			<style>
		        table {
		            font-family: arial, sans-serif;
		            border-collapse: collapse;
		        }
		        td, th {
		            border: 1px solid #dddddd;
		            text-align: left;
		            padding: 5px;
		        }
		      	th.id {
		      		padding: 5px;
		      		width: 10%;
		      	}
		        tr:nth-child(even) {
		            background-color: #dddddd;
		        }
        	</style>
		</head>
		<body>
			<h1>Welcome to your ToDoList app</h1>
			
			<form action="creating" method="post">
				<fieldset>
					<legend><strong>Adding New Task</strong></legend>
					<div>
					Description:

					<br>

					<textarea rows="3" cols="40" name="task"></textarea>

					<br>
					
					<input type="checkbox" name="isdone" value="yes"> Mark as Done
					</div>
					
					<br>

					<input type="submit" value="Save changes">
					<input type="reset" value="Discard changes" id="hello">
				</fieldset>
			</form>
				
				<br>

			<form action="updating" method="put">
				<fieldset>
					<legend><strong>Editing a Task</strong></legend>
					<div>
					Task's Number(limited to one): 

					<br>
					
					<input type="text" name="id">

					<br>
					Description:

					<br>

					<textarea rows="3" cols="40" name="task"></textarea>
					
					<br>

					<input type="checkbox" name="isdone" value="yes"> Mars as Done
					</div>

					<br>

					<input type="submit" value="Save changes">
					<input type="reset" value="Discard changes">
				</fieldset>
			</form>
				
				<br>

			<form action="removing" method="post">
				<fieldset>
					<legend><strong>Deleting a Task</strong></legend>
					<div>
					Task's Number(limited to one): 
					
					<br>

					<input type="text" name="task_id">
					</div>
				

				<br>

				<input type="submit" value="Save changes">
				<input type="reset" value="Discard changes">
				</fieldset>
			</form>

				<br><br>
				<h2>What should I do?</h2>

				<table style="width:100%">
				  <tr>
				    <th class='id'>Number</th>
				    <th class='description'>Description</th>
				  </tr>
	"""
	return html_static_part
				  
def creating_table_rows_string(data_base, class_name):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""
	data = data_base.session.query(class_name.id, class_name.task, class_name.isdone).order_by(class_name.isdone).all()
	tasks_list=[]
	counter=0
	for item in data:
		if item[2] == '0':
			text = "<tr><td>{0}</td><td>{1}</td></tr>".format(item[0], item[1])
			tasks_list.append(text)
			if data[counter+1][2] == '1':
				tasks_list.append("""</table><br><h2>Done.</h2><table style="width:100%">
					<tr><th class='id'>Number</th><th class='description'>Description</th></tr>""")
		else:
			text = "<tr><td>{0}</td><td>{1}</td></tr>".format(item[0], item[1])
			tasks_list.append(text)
		counter+=1
	html_changing_part = ''
	for item in tasks_list:
		html_changing_part += item
	return html_changing_part

def create_full_html_string(html_static_part, html_changing_part):
	"""
	This fuction takes all the parts of the HTML String and combine them into one FULL HTML String.
	"""
	closer="""</table></body></html>"""
	full_html = html_static_part + html_changing_part + closer
	return full_html

def return_full_html(data_base, class_name):
	"""
	This function returns the full HTML String.
	The purpose here is to be able to call just one function when we want to render 
	the	Homepage's HTML String (instead of 3 functions)
	"""
	html_static_part = static_html_string()
	html_changing_part = creating_table_rows_string(data_base, class_name)
	full_html = create_full_html_string(html_static_part, html_changing_part)
	return full_html

def get_all_tasks(data_base, class_name):
	"""
	This function querying all the taks from Tasks table.
	"""
	get_all_tasks_query = data_base.session.query(class_name.id, class_name.isdone, class_name.task).all()
	return(get_all_tasks_query)

def insert_into_db(data_base, class_name, task_description_to_insert, task_status_to_insert):
	if task_status_to_insert == 'yes':
		task_status_to_insert = '1'
	else:
		task_status_to_insert = '0'
	NewTask = class_name(task_description_to_insert, task_status_to_insert)
	data_base.session.add(NewTask)
	data_base.session.commit()

def remove_from_db(data_base, class_name, task_to_remove):
	get_task_to_remove = data_base.session.query(class_name.id).filter_by(id=task_to_remove)
	get_task_to_remove.delete()
	data_base.session.commit()