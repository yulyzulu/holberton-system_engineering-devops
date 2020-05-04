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

    for i in employee_json:
        lista = []
        data[i.get('id')] = lista
        for j in task_json:
            if j.get('userId') == i.get('id'):
                dic = {}
                dic["task"] = j.get('title')
                dic["completed"] = j.get('completed')
                dic["username"] = i.get('username')
                lista.append(dic)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
