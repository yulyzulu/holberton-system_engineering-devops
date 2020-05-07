#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    reddit = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    user = {'user-agent': 'X-Modhash'}
    request = requests.get(reddit, headers=user)
    if request.history or request.status_code == 404:
        print("None")
    else:
        json_reddit = request.json()
        children_list = json_reddit.get('data').get('children')
        for i in children_list:
            print(i.get('data').get('title'))
