import requests
import json


def top_ten(subreddit):
    if subreddit is None:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/top.json"

    headers = {
        'User-Agent': 'MyRedditSubCounter/1.0 (by /u/obams)'
    }

    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False)
        response.raise_for_status()  # exception for 4xx / 5xx status codes
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            titles = [post['data']['title'] for post in posts]
            top_10_titles = titles[:10]

            for title in top_10_titles:
                print(title)
        else:
            print(f"No posts found for subreddit '{subreddit}'")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
