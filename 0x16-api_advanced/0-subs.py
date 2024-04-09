#!/usr/bin/python3
""" Working with Advanced APIs """

import requests


def number_of_subscribers(subreddit):
    """ get number of subscriber for a subreddit """
    # construct url and subreddit to call
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # define customer User-Agent to avoid errors due to many requests
    headers = {'User-Agent': 'Custom-User-Agent'}
    # make an api call using request to get details about a subreddit
    response = requests.get(url, headers=headers)

    # check the staus of the call
    if response.status_code == 200:
        # extract the subscribers count from the json file
        data = response.json()
        subscribers = data['data'].get('subscribers')
        return subscribers
    else:
        # return 0 for invalid subreddits or any other errors
        return 0
