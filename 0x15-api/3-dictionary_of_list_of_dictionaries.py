#!/usr/bin/python3
"""A python script that using REST API for a given employee ID
returns information bout his/her TODO list progress.
"""

import csv
import json
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
    except requests.exceptions.RequestException as error:
        printf(f"An error occurred while fetching TODOs: {error}")
        return None


def fetch_todos_no_id():
    """
    Fetch a list of todos data from the todoAPI
    Returns:
        A list of dictionary representing TODO data, None if error
    """
    try:
        todos_response = requests.get(
            todos_url)
        if todos_response.status_code == 200:
            return todos_response.json()
        else:
            print(
                f"Error retrieving TODOs"
                f"Response code: {todos_response.status_code}")
    except requests.exceptions.RequestException as error:
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
          f" is done with tasks({completed_tasks}/{total_tasks}):")
    for title in titles:
        print(f"\t {title}")


def write_to_csv(user_id, username, tasks):
    """
    Writes task information to a csv file
    Args:
        user_id (int): The ID of the user
        username (str): The name of the user
        task (list): A list of dictionaries representing tasks
    """
    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            completed_status = "True" if task["completed"] else "False"
            task_title = task["title"]
            writer.writerow([user_id, username, completed_status, task_title])


def write_to_json(user_id, username, tasks):
    """writes task information to a JSON file."""
    filename = f"{user_id}.json"
    data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username,
            } for task in tasks
        ]
    }
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def write_full_details_toJSON(users, todos):
    """
    Writes all task information to a JSON file
    Args:
        users (list): A list of dictionaries representing users
        todos (list): A list of dictionaries representing tasks
    """
    filename = "todo_all_employees.json"
    data = {}
    for user in users:
        user_id = user["id"]
        user_todos = [todo for todo in todos if todo["userId"] == user_id]
        task_list = []
        for task in user_todos:
            task_list.append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            })
        data[str(user_id)] = task_list

    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def main():
    """
    Entry point for the script
    Handles user input and function calls
    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    users = get_users()
    if not users:
        return 1

    todos = fetch_todos_no_id()
    if not todos:
        return 1

    write_full_details_toJSON(users, todos)


if __name__ == "__main__":
    main()
