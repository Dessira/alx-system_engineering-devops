#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    storage = {}

    for user in users:
        eid = user.get("id")
        username = user.get("username")
        all_tasks = []

        for task in tasks:
            if (task.get("userId") == eid and task.get("completed")):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = username
                all_tasks.append(temp)

        storage[eid] = all_tasks

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(storage, jsonfile)
