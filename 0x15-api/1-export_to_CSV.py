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
    formato = []

    with open(sys.argv[1] + ".csv", mode='w') as csv_file:
        formato = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for i in task_json:
            if int(sys.argv[1]) == (i.get('userId')):
                #formato = csv.writer(int(sys.argv[1]).csv, delimiter=',', quotechar='"', quioting=csv.QUOTE_ALL)
                for j in employee_json:
                    if int(sys.argv[1]) == j.get('id'):
                       # formato = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                        formato.writerow([j.get('id'), j.get('username'), i.get('completed'), i.get('title')])
