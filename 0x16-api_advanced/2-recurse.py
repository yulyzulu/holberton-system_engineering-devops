#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """function that queries the Reddit API and return
       a list containing the titles"""
    reddit = 'https://www.reddit.com/r/{}/hot.json?after={}\
'.format(subreddit, after)
    user = {'user-agent': 'X-Modhash'}
    request = requests.get(reddit, headers=user)

    if request.history or request.status_code == 404:
        return None
    json_reddit = request.json()
    new_after = json_reddit.get('data').get('after')

    if new_after:
        children_list = json_reddit.get('data').get('children')
        for i in children_list:
            title = i.get('data').get('title')
            hot_list.append(title)
        return recurse(subreddit, hot_list, after=new_after)
    else:
        return hot_list
