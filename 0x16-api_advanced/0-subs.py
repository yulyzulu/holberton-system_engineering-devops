#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return number of suscribers"""
    reddit = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'user-agent': 'X-Modhash'}
    request = requests.get(reddit, headers=user)
    if request.history or request.status_code == 404:
        return 0
    else:
        json_reddit = request.json()
        return json_reddit.get('data').get('subscribers')
