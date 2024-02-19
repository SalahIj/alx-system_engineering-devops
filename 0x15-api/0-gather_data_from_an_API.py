#!/usr/bin/python3
""" The necessery imported modules """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_Id = sys.argv[1]
    url_user = "{}/users/{}".format(url, user_Id)
    user_info = requests.get(url_user)

    name = user_info.json().get("name")

    to_do = requests.get("{}/todos".format(url))
    Total = 0
    finished = 0

    for task in to_do.json():
        if task.get("userId") == int(user_Id):
            Total += 1
            if task.get("completed"):
                finished += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, finished, Total))

    print("\n".join(["\t " + task.get("title") for task in to_do.json()
          if task.get("userId") == int(user_Id) and task.get("completed")]))
