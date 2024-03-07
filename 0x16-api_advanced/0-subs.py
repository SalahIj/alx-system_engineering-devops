#!/usr/bin/python3
""" The imported modules """


def number_of_subscribers(subreddit):
    """ The function definition
    Args:
       subreddit: the input
    """
    import requests

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub_info = requests.get(URL,
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
