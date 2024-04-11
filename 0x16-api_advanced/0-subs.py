#!/usr/bin/python3
"""
This module is for getting the number of subscribers of a certain subreddit.
"""
from requests import get


def number_of_subscribers(subreddit):
    """ function to get subscriber count"""
    if subreddit and type(subreddit) is str:
        subscribers = 0
        url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        req = get(url, headers=headers)
        if req.status_code == 200:
            data = req.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers