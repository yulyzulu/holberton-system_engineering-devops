#!/usr/bin/python3
"""Script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress"""


import requests
import sys

if __name__ == "__main__":

    number_task = 0
    task_done = 0
    title_task = []
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    employee = requests.get('https://jsonplaceholder.typicode.com/users')
    task_json = tasks.json()
    employee_json = employee.json()

    for i in task_json:
        if int(sys.argv[1]) == (i.get('userId')):
            number_task = number_task + 1
            if i.get('completed') is True:
                task_done = task_done + 1
                title_task.append(i.get('title'))

    for j in employee_json:
        if int(sys.argv[1]) == j.get('id'):
            print("Employee {} is done with tasks({}/{}\
):".format(j['name'], task_done, number_task))
            for x in title_task:
                print("	 {}".format(x))
