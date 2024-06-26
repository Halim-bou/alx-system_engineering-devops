#!/usr/bin/python3
"""
function that queries the
Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


headers = {"User-Agent": "my_user_agent"}


def top_ten(subreddit):
    """method to retrieve the post from given dubreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 200 and response.text:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
