#!/usr/bin/python3
""" imported modules """
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ The function definition
    Args:
        subreddit:
        hot_list:
        count:
        after:
    """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    Agent_user = {"User-Agent": "My-User-Agent"}
    parmmeters = {"count": count, "after": after}
    Groupe_info = requests.get(URL, params=parmmeters,
                               headers=Agent_user, allow_redirects=False)

    if Groupe_info.status_code >= 400:
        return None

    listt = hot_list
    for child in Groupe_info.json().get("data").get("children"):
        listt.append(child.get("data").get("title"))

    info = Groupe_info.json()
    if not info.get("data").get("after"):
        return listt

    return recurse(subreddit, listt, info.get("data").get("count"),
                   info.get("data").get("after"))
