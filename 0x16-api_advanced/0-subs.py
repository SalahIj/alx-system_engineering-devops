#!/usr/bin/python3
"""-----------------"""
import requests


def number_of_subscribers(subreddit):
    """____________________________________________________________
    ----------------"""

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    Agent_user = {"User-Agent": "My-User-Agent"}
    Groupe_info = requests.get(URL, headers=Agent_user, allow_redirects=False)
    if Groupe_info.status_code >= 300:
        return 0

    return Groupe_info.json().get("data").get("subscribers")
