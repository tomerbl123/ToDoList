function incompleteTasksToTable(table, array){
    if(array.length === 0){
        var noTasksHeadline = document.createElement('h2');
        noTasksHeadline.innerHTML = "<h2>Nothing To Do..</h2>";
        table.parentNode.replaceChild(noTasksHeadline, table);
    }
    else{
        var tableData = "<thead><tr><th>Number</th><th>Description</th></tr></thead><tbody>";
        var tasksHeadline = document.createElement('h2');
        tasksHeadline.innerHTML = "<h2>What Should I do?</h2>";
        for(i=0; i<array.length; i++){
            tableData += "<tr>";
            tableData += "<td>" + Object.keys(array[i])[0] + "</td>";
            tableData += "<td>" + Object.values(array[i])[0] + "</td>";
            tableData += "</tr>";
        }
    tableData += "</tbody>";
    table.innerHTML = tableData;
    document.body.insertBefore(tasksHeadline, table);
    }}

function doneTasksToTable(table, array){
    if(array.length === 0){
        table.parentNode.removeChild(table);
    }
    else{
        var tableData = "<thead><tr><th>Number</th><th>Description</th></tr></thead><tbody>";
        var doneTasksHeadline = document.createElement('h2');
        doneTasksHeadline.innerHTML = "<h2>Great Success!</h2>";
        for(i=0; i<array.length; i++){
            tableData += "<tr>";
            tableData += "<td>" + Object.keys(array[i])[0] + "</td>";
            tableData += "<td>" + Object.values(array[i])[0] + "</td>";
            tableData += "</tr>";
        }
    tableData += "</tbody>";
    table.innerHTML = tableData;
    document.body.insertBefore(doneTasksHeadline, table);
    }}

incompleteTasksToTable(IncompleteTasks, incompleteTasksArray)
doneTasksToTable(DoneTasks, doneTasksArray)