#!/usr/bin/python3
"""Accesses a REST-API for the ToDo lists of the employees"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    EMPLOYEE_NAME = response.json().get('name')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()
    NUMBER_OF_DONE_TASKS = 0
    done_tasks_list = []

    for task in tasks:
        if task.get('completed'):
            done_tasks_list.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(tasks)))

    for task in done_tasks_list:
        print("\t {}".format(task.get('title')))
