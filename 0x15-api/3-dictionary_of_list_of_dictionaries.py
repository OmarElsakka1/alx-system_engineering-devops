#!/usr/bin/python3
"""Exporting To-Do list information of the whole employees to a JSON file."""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
