#!/usr/bin/python3
"""task0 module"""

import requests
import json
import sys


user = requests.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
user = user.json()
todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}')
todos = todos.json()
#print(todos.json())
name = user['name']
total_tasks = len(todos)
tasks_done = 0
lists_of_titles = []
for f in todos:
    if user['id'] == f['userId']:
        total_tasks += 1
        if f['completed']:
            tasks_done += 1
            lists_of_titles.append(f['title'])
    #print(f"****{f}****")    
print(f"Employee {name} is done with tasks({tasks_done}/{total_tasks})")
for title in lists_of_titles:
    print(f"\t{title}")
