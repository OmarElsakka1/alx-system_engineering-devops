#!/usr/bin/python3
"""
    This module is for getting the titles of all hot \
        articles for a certain subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    else:
        sub_url = f'hot.json?limit=100&after={after}'
        url = f'https://www.reddit.com/r/{subreddit}/{sub_url}'
    headers = {'User-Agent': 'by u/qasqot79'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
