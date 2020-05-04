#!/usr/bin/python3
"""Script to export data in the json format"""

import json
import requests
import sys

if __name__ == "__main__":

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    employee = requests.get('https://jsonplaceholder.typicode.com/users')
    task_json = tasks.json()
    employee_json = employee.json()
    data = {}
    lista = []

    for i in task_json:
        if i.get('userId'):
            data = {i.get('userId'): lista}
            for j in employee_json:
                if j.get('id'):
                    lista.append({
                        'task': i.get('title'),
                        'completed': i.get('completed'),
                        'username': j.get('username')})

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
