#!/usr/bin/python3
""" fetsh data from JSON API"""
import requests
from sys import argv
import json

# args = argv[1]
data = f'https://jsonplaceholder.typicode.com/'

print(data)
args = argv[1]
user_id = f'users?id={args}'
todo_list = f'todos?user_id={args}'
completed = f'{todo_list}?completed=True'
non_completed = f'{todo_list}?completed=False'
num_of_tasks = len(completed) + len(non_completed)
user_data = requests.get(f'{data}{user_id}').json()
todosData = requests.get(f'{data}{todo_list}').json()
todosDone = requests.get(f'{data}{completed}').json()
name = user_data[0].get('name')
print(f'Employee {name} is done with tasks({len(completed)}/{num_of_tasks}):')
for task in todosDone:
    print(f'\t ' + task.get('title'))
