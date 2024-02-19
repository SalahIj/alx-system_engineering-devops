#!/usr/bin/python3
"""-------------------------------------------------
------------------------"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    Id_user = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, Id_user))
    name = user.json().get('username')
    to_do = requests.get('{}/todos'.format(url))
    tasks = to_do.json()

    filename = Id_user + '.csv'
    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in tasks:
            if task.get('userId') == int(Id_user):
                finished = task.get('completed')
                title = task.get('title')
                writer.writerow([Id_user, name, str(finished), title])
