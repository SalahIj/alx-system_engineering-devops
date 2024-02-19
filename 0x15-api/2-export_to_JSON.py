#!/usr/bin/python3
"""-------------------------------------------------
------------------------"""

import json
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com"
    Id_user = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, Id_user))
    to_do = requests.get("{}/todos".format(url))
    tasks = to_do.json()

    User_to_do = {}
    List_of_task = []

    for task in tasks:
        if task.get("userId") == int(Id_user):
            Title = task.get("title")
            Completed = task.get("completed")
            Username = user.json().get("username")
            Dict_of_task = {"task": Title,
                            "completed": Completed,
                            "username": Username}
            List_of_task.append(Dict_of_task)
    User_to_do[Id_user] = List_of_task

    filename = Id_user + ".json"
    with open(filename, mode="w") as file:
        json.dump(User_to_do, file)


if __name__ == "__main__":
    main()
