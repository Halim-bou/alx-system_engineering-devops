#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """function that retrieve the subreddit fiven subscribers"""
    headers = {'User-Agent': 'Custom User-Agent'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return 0

        data = response.json()

        subscribers = data['data']['subscribers']

        return subscribers

    except Exception as e:
        return 0
