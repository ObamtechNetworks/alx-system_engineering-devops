#!/usr/bin/python3
""" Working with Advanced APIs """
import requests


def top_ten(subreddit):
    """ get number of subscriber for a subreddit """
    if subreddit is None:
        print(None)
    # construct url and subreddit to call
    url = f"https://www.reddit.com/r/{subreddit}/top.json"

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
            # print the top 10 posts
            posts = data['data']['children']
            titles = [post['data']['title'] for post in posts]

            # extract top 10
            top_10_titles = titles[:10]

            # print the to_10
            for title in top_10_titles:
                print(title)
        else:
            # return 0 for invalid subreddits or any other errors
            print(None)
    except (Exception, JSONDecodeError) as e:
        print(None)
