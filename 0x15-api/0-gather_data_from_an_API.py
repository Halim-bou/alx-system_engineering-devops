#!/usr/bin/python3
""" fetsh data from JSON API"""
import requests
import sys

def main():
    """function that list of completed task using api json"""
    url = f'https://jsonplaceholder.typicode.com/'
    args = sys.argv[1]
    user = f'users?id={args}'
    todoList = f'todos?user_id={args}'
    completed = f'{todoList}&completed=true'
    # non_completed = f'{todo_list}&completed=false'
    userData = requests.get(f'{url}{user}').json()
    todosData = requests.get(f'{url}{todoList}').json()
    todosDone = requests.get(f'{url}{completed}').json()
    sumOfTasks = len(todosDone) + len(todosData)
    Name = userData[0].get('name')
    print(f'Employee {Name} is done with tasks({len(todosDone)}/{sumOfTasks}):')
    for task in todosDone:
        print(f'\t ' + task.get('title'))


if __name__ == "__main__":
    main()
