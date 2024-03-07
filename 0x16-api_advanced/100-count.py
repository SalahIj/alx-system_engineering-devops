#!/usr/bin/python3
"""imported modules"""
from requests import get


def sort_key(item):
    """--------------"""
    return (-item[1], item[0])


def count_words(subreddit, word_list=[], after=None, cleaned_dict=None):
    """
    function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript, but java should not).
    """

    lst = []
    for i in word_list:
        lst.append(i.casefold())
    list_cleaned = list(dict.fromkeys(lst))

    if cleaned_dict is None:
        cleaned_dict = dict.fromkeys(list_cleaned)

    if subreddit is None or not isinstance(subreddit, str):
        return None

    URL = "https://www.reddit.com/r/{}/hot/.json?after={}".format(subreddit,
                                                                  after)

    get_info = get(URL,
                   headers={"User-agent": "My-User-Agent"},
                   params={"show": "all"})

    if get_info.status_code != 200:
        return None

    data = get_info.json()
    ligne1 = data.get("data").get("children")
    after = data.get("data").get("after")

    if after is None:
        new = {}
        for k, v in cleaned_dict.items():
            if v is not None:
                new[k] = v

        for k in sorted(new.items(), key=sort_key):
            print("{}: {}".format(k[0], k[1]))

        return None

    for i in ligne1:
        title = i.get("data").get("title")
        title_splited1 = title.split()
        title_splited2 = [i.casefold() for i in title_splited1]

        for j in title_splited2:
            if j in cleaned_dict and cleaned_dict[j] is None:
                cleaned_dict[j] = 1
            elif j in cleaned_dict and cleaned_dict[j] is not None:
                cleaned_dict[j] += 1

    count_words(subreddit, word_list, after, cleaned_dict)
