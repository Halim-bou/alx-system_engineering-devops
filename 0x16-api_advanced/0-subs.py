#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """function that retrieve the subreddit fiven subscribers"""
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json()

        subscribers = data['data']['subscribers']

        return subscribers

    except Exception as e:
        return 0
