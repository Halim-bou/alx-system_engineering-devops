#!/usr/bin/python3
""" fetsh data from JSON API"""
import requests
from sys import argv

def completed_todos():
    """function that list of completed task using api json"""
    data = f'https://jsonplaceholder.typicode.com/'
    args = argv[1]
    user_id = f'users?id={args}'
    todo_list = f'todos?user_id={args}'
    completed = f'{todo_list}?completed=True'
    non_completed = f'{todo_list}?completed=False'
    user_data = requests.get(f'{data}{user_id}').json()
    todosData = requests.get(f'{data}{todo_list}').json()
    todosDone = requests.get(f'{data}{completed}').json()
    num_of_tasks = len(todosDone) + len(todosData)
    name = user_data[0].get('name')
    print(f'Employee {name} is done with tasks({len(todosDone)}/{num_of_tasks}):')
    for task in todosDone:
        print(f'\t ' + task.get('title'))


if __name__ == "__main__":
    completed_todos()
