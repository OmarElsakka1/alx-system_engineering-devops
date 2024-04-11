#!/usr/bin/python3
"""
This module is for getting the number of subscribers of a certain subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)