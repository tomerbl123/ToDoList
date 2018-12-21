def get_all_tasks(data_base, class_name):
	"""
	This function querying all the taks from Tasks table.
	"""
	get_all_tasks_query = data_base.session.query(class_name.id, class_name.isdone, class_name.task).all()
	return(get_all_tasks_query)

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
			<h1>Welcome to your ToDoList</h1>
			<h2>Here you can add or edit tasks</h2>
			
			<form action="creating" method="post">
				<fieldset>
					<legend><strong>Adding/Editing Tasks</strong></legend>
					<div>
					Description: <input type="text" name="task">
					<input type="checkbox"> Mark as Done
					</div>
					
					<br><br>

					<input type="submit" value="Save changes">
					<input type="reset" value="Discard changes" id="hello">
				</fieldset>

				<br><br>
				<h2>Here are your Tasks</h2>

				<table style="width:100%">
				  <tr>
				    <th class='id'>ID</th>
				    <th class='isdone'>Is Done?</th>
				    <th class='description'>Description</th>
				  </tr>
	"""
	return html_static_part

def creating_table_rows_string(data_base, class_name):
	"""
	This function creates the dynamic part of the HTML String.
	Meaning, it creates table rows according to the amount of tasks that we have.
	"""
	data = data_base.session.query(class_name.id, class_name.isdone, class_name.task).all()
	tasks_list=[]
	for item in data:
		text = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(item[0], item[1], item[2])
		tasks_list.append(text)
	html_changing_part = ''
	for item in tasks_list:
		html_changing_part += item
	return html_changing_part

def create_full_html_string(html_static_part, html_changing_part):
	"""
	This fuction takes all the parts of the HTML String and combine them into one FULL HTML String.
	"""
	closer="""</table></form></body></html>"""
	full_html = html_static_part + html_changing_part + closer
	return full_html