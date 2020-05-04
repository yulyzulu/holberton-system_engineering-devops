#!/usr/bin/python3
"""Export data in the json format"""

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
    data = {sys.argv[1]: lista}

    for i in task_json:
        if int(sys.argv[1]) == (i.get('userId')):
            for j in employee_json:
                if int(sys.argv[1]) == j.get('id'):
                    lista.append({
                        'task': i.get('title'),
                        'completed': i.get('completed'),
                        'username': j.get('username')})

    with open(sys.argv[1] + ".json", 'w') as json_file:
        json.dump(data, json_file)
