#!/usr/bin/python3
"""A python script that using REST API for a given employee ID
returns information bout his/her TODO list progress.
"""

import requests

users_url = "https://jsonplaceholder.typicode.com/users"


def employee_todo_progress(employee_id):
    """ function that fetches user data and todo information from
    APIs, calculates and display the employee TODO list progress

    Args:
        employee_id (int): The ID of the employee to retrieve data for.
    """
    # fetch users and find target_emp from users_url
    users_response = requests.get(users_url)

    # check response code
    if users_response.status_code == 200:
        # save users response as json
        users = users_response.json()
        # from the json, find the target employee data based on id
        for user in users:
            if user["id"] == employee_id:
                target_emp = user
                break
        else:
            print(users.response.status_code)
            return

    # fetch TODO list data from the todos url
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    # get data by sending a get request
    todos_response = requests.get(todos_url)
    # check if the request was successful
    if todos_response.status_code == 200:
        todos = todos_response.json()
        # Filter TODOs based on the target employee, store it in a list
        employee_todos = [
            todo for todo in todos if todo['userId'] == employee_id]
        # calculate task progress completed and uncompleted
        comp_tasks = sum(
                todo["completed"] for todo in employee_todos)
    else:
        print(todos_response.status_code)
        return

    total_tasks = len(employee_todos)
    # display the progress
    print(
        f"Employee \
{target_emp['name']} is done with tasks({comp_tasks}/{total_tasks}):")

    for task in employee_todos:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
            employee_todo_progress(employee_id)
        except Exception as e:
            print(str(e))
