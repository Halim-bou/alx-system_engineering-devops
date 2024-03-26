#!/usr/bin/python3
""" fetsh data from JSON API"""
import json
import requests
import sys


if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/'
    if len(sys.argv) > 1:
        args = sys.argv[1]
        user = f'users?id={args}'
        todoList = f'todos?userId={args}'
        userData = requests.get(f'{url}{user}').json()
        name = userData[0].get("username")
        todosData = requests.get('{}{}'.format(url, todoList)).json()
        with open(f'{args}', 'w', newline="") as f:
            dict_list = []
            for todo in todosData:
                new_d = {}
                new_d['task'] = todo.get('title')
                new_d['completed'] = todo.get('completed')
                new_d['username'] = name
                dict_list.append(new_d)
            dict_json = {}
            dict_json[args] = dict_list
            json.dump(dict_json, f)
