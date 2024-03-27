#!/usr/bin/python3
"""A python script that using REST API for a given employee ID
returns information bout his/her TODO list progress.
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def get_users():
    """
    function that fetches user data in json format
    Args:
        user_id (int): The ID of the user to retrieve data
    Return:
        A list of dictionaries representing usr data, None if error occurred
    """
    # fetch users and find target_emp from users_url
    try:
        users_response = requests.get(users_url)
        # check response code
        if users_response.status_code == 200:
            # save users response as json
            users = users_response.json()
            return users
        else:
            print(f"Error retrieving users: {users_response.status_code}")
            return None
    except requests.exceptions.RequestException as error:
        print(f"An error occurred while fetching users: {error}")
        return None
    # from the json, find the target employee data based on id
    for user in users:
        if user["id"] == employee_id:
            target_emp = user
            break


def get_todos(employee_id):
    """
    Gets a list of todos data from the todoAPI based on a given employee_id
    Args:
        employee_id (int): The ID of the employee to retrieve his/her todo
    Returns:
        A lisit of dictionary represeenting TODO data, None if error
    """
    try:
        todos_response = requests.get(
            todos_url, params={"userId": employee_id})
        if todos_response.status_code == 200:
            return todos_response.json()
        else:
            print(
                f"Error retrieving TODOs for employee {employee_id}"
                f"Response code: {todos_response.status_code}")
    except request.exceptions.RequestException as error:
        printf(f"An error occurred while fetching TODOs: {error}")
        return None


def calc_emp_todo_progress(employee_todos):
    """
    Function that calculates employee todo progress based on
    the given list of employee todos
    Args:
        employee_todos (list): A list of dictionaries representing TODOdata
    Returns:
        tuple: A tuple for the no of completed tasks and total no of tasks
    """
    completed_tasks = sum(todo['completed'] for todo in employee_todos)
    total_tasks = len(employee_todos)
    return completed_tasks, total_tasks


def display_progress(employee_name, completed_tasks, total_tasks, titles):
    """Displays a formatted employee TODO list progress information.
    Args:
        employee_name (str): The name of the employee.
        completed_tasks (int): The number of completed tasks.
        total_tasks (int): The total number of tasks.
        titles (list): A list of titles of completed TODOs.
    """
    print(f"Employee {employee_name}"
          f" is done with tasks({completed_tasks}/{total_tasks})")
    for title in titles:
        print(f"\t{title}")


def main():
    """
    Entry point for the script
    Handles user input and function calls
    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """

    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print(f"Cannot convert value to int: {sys.argv[1]}")
            return 1

        users = get_users()
        if not users:
            return 1

        target_employee = None
        for user in users:
            if user["id"] == employee_id:
                target_employee = user
                break
        if not target_employee:
            print(f"Employee with ID {employee_id} not found")
            return 1

        todos = get_todos(employee_id)
        if not todos:
            return 1

        completed_tasks, total_tasks = calc_emp_todo_progress(todos)
        completed_todo_titles = [
            todo["title"] for todo in todos if todo["completed"]]

        display_progress(
            target_employee["name"],
            completed_tasks,
            total_tasks,
            completed_todo_titles)


if __name__ == "__main__":
    main()
