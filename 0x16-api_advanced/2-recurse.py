#!/usr/bin/python3

"""Recursively request data from an api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves hot article titles from a given sbreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "YourRedditAppName"}  # Replace with your appnamee
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None  # Subreddit not found

    data = response.json()

    if "data" not in data or "children" not in data["data"]:
        return None  # Handle unexpected API response structure

    after = data["data"].get("after")
    posts = data["data"]["children"]

    for post in posts:
        title = post["data"]["title"]
        hot_list.append(title)

    if after:
        recurse(subreddit, hot_list, after)  # Recursive call for next page

    return hot_list
