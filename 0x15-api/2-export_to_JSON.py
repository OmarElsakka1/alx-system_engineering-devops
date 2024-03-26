#!/usr/bin/python3
"""Accesses a REST-API for the ToDo lists of the employees
and save it in a JSON file"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()

    dictionary = {employee_Id: []}
    for task in tasks:
        dictionary[employee_Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_Id), 'w') as filename:
        json.dump(dictionary, filename)
