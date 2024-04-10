#!/usr/bin/python3
"""
ecursive function that queries the
Reddit API and returns a list containing
the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    headers = {"User-Agent": "project_user_agent"}
    params = {"after": hot_list}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        hot_list = data["data"]["after"]
        if hot_list is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, hot_list)
        all_posts.extend(next)
        return all_posts
    return None
