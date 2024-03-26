#!/usr/bin/python3
""" fetsh data from JSON API"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    if len(sys.argv) > 1:
        args = sys.argv[1]
        user = f'users?id={args}'
        todoList = f'todos?userId={args}'
        userData = requests.get(f'{url}{user}').json()
        name = userData[0].get("name")
        todosData = requests.get('{}{}'.format(url, todoList)).json()
        with open(f'{args}.csv', 'w', newline="") as csvf:
            writer = csv.writer(csvf, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            writer.writerows([args,
                              name,
                              task.get('completed'),
                              task.get('title')] for task in todosData)
