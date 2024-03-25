#!/usr/bin/python3
""" fetsh data from JSON API"""
import requests
import sys


def main():
    """function that list of completed task using api json"""

    if len(sys.argv) != 2:
        return

    url = f'https://jsonplaceholder.typicode.com/'
    args = sys.argv[1]
    user = f'users?id={args}'
    todoList = f'todos?userId={args}'
    completed = f'{todoList}&completed=true'
    userData = requests.get(f'{url}{user}').json()
    name = userData[0].get("name")

    if name is None:
        return

    todosData = requests.get(f'{url}{todoList}').json()
    todosDone = requests.get(f'{url}{completed}').json()
    lenDone = len(todosDone)
    lenData = len(todosData)
    print(f'Employee {name} is done with tasks({lenDone}/{lenData}):')
    for task in todosDone:
        print(f'\t ' + task.get("title"))


if __name__ == "__main__":
    main()
