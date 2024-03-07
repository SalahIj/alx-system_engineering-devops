#!/usr/bin/python3
"""-----------------"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    Agent_user = {"User-Agent": "My-User-Agent"}
    sub_info = requests.get(URL, headers=Agent_user,
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
