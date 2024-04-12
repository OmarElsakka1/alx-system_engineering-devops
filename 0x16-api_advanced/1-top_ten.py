#!/usr/bin/python3
"""
This module is for getting the first 10 hot posts for a certain subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Getting the top 10 of thhe given subreddit
    """

    headers = {
            "Accept": "*/*",
            "User-Agent": "ALX student script",
    }
    api_url = 'https://www.reddit.com/r'
    type_ = 'hot'
    url = '{}/{}/{}.json?raw_json=1&limit=10'.format(
        api_url, subreddit, type_
    )
    res = requests.get(url, headers=headers)
    if not res.ok:
        print(None)
    else:
        data = res.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post['data']["title"]
            print(title)
