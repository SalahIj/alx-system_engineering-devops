#!/usr/bin/python3
""" Imported modules """
import requests


def top_ten(subreddit):
    """ The function definition """
    try:
        headers = {"User-Agent": "My-User-Agent"}
        resp = requests.get("https://www.reddit.com/r/{}/hot.json".
                            format(subreddit),
                            headers=headers,
                            allow_redirects=False)
        if resp.status_code == 404:
            print("None")
            return 0
        request = resp.json().get("data").get("children")
        for i in range(10):
            print(request[i].get("data").get("title"))
    except Exception:
        print("None")
        return 0
