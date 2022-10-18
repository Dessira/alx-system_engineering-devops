#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    eid = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(eid)).json().get("username")
    all_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(eid)):
            temp = []
            temp.extend((eid,
                         username,
                         task.get("completed"),
                         task.get("title")))
            all_tasks.append(temp)

    with open("{}.csv".format(eid), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
