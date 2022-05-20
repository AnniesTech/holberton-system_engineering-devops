#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
Python script that, using https://jsonplaceholder.typicode.com,
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()

    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()

    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('tittle'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
