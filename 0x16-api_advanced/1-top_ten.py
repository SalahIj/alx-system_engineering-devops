#!/usr/bin/python3
""" Imported modules """
import requests


def top_ten(subreddit):
    """ The function definition """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0\
            (by /u/Large_Alternative_30)",
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if (response.status_code == 404):
            print('None')
            return 0
        request = response.json().get('data').get('children')
        for i in range(10):
            print(request[i].get('data').get('title'))
    except Exception:
        print('None')
        return 0
