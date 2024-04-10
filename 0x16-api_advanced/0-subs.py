#!/usr/bin/python3
"""Working with Advanced APIs"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscriber for a subreddit"""
    if subreddit is None:
        return 0
    # construct url and subreddit to call
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # define customer User-Agent to avoid errors due to many requests
    headers = {
            'User-Agent': '"MyRedditSubCounter/1.0 (by /u/obams)"'}
    # make an api call using request to get details about a subreddit
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # check the staus of the call
        if response.status_code == 200:
            # extract the subscribers count from the json file
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # return 0 for invalid subreddits or any other errors
            return 0
    except Exception as e:
        print('Error: {}'.format(e))
        return 0
