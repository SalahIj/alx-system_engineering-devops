#!/usr/bin/python3
"""-------------------------------------------------
------------------------"""

import json
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com"
    Users = requests.get("{}/users".format(url)).json()
    Tasks = requests.get("{}/todos".format(url)).json()

    All_to_do = {}

    for user in Users:
        List_of_tasks = []
        for task in Tasks:
            if task.get("userId") == user.get("id"):
                User = user.get("username")
                Title = task.get("title")
                Completed = task.get("completed")
                Dict_of_tasks = {"username": User,
                                 "task": Title,
                                 "completed": Completed}
                List_of_tasks.append(Dict_of_tasks)
        All_to_do[user.get("id")] = List_of_tasks

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(All_to_do, file)


if __name__ == "__main__":
    main()
