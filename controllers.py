def get_all_tasks():
	#here we will get all the tasks.
	q = db.session.query(class_name.id, class_name.task, class_name.isdone).all()
	print(q)
	return(q)

def static_html_rendering():
	html_static_part = """\
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

def arrange_tasks_in_html_tr():
	"""
	here we will take each task and arrange it in table rows.
					  <tr>
				    <td>Jill</td>
				    <td>Smith</td> 
				    <td>50</td>
				  </tr>
	"""
	for item in q:
		TBC
		return(html_changing_part)


def combine_static_html_with_dinamic_rows(html_static_part, html_):
	#here we will combine the static html structure with the changing amount of tasks.
	html_static_part
	html_changing_part
	closer="""\
				</table>
			</form>
		</body>
	</html>
	"""
	pass