#!/usr/bin/python3
"""Export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    employee = requests.get('https://jsonplaceholder.typicode.com/users')
    task_json = tasks.json()
    employee_json = employee.json()
    data = []

    with open(sys.argv[1] + ".csv", mode='w') as csv_file:
        data = csv.writer(csv_file, delimiter=',', quotechar='"\
', quoting=csv.QUOTE_ALL)
        for i in task_json:
            if int(sys.argv[1]) == (i.get('userId')):
                for j in employee_json:
                    if int(sys.argv[1]) == j.get('id'):
                        data.writerow([j.get('id'), j.get('usernam\
e'), i.get('completed'), i.get('title')])
