#!/usr/bin/python3
"""
To export data in CSV format
"""

if __name__ == '__main__':

    import csv
    import requests
    from sys import argv

    csv_path = "USER_ID.csv"
    url = "https://jsonplaceholder.typicode.com/"
    param = argv[1]
    user = requests.get(url + "users?id={}".format(param))
    # Transforms JSON data in Python objects
    user = user.json()
    # Gets the name from the user object
    name = user[0]["username"]
    todos = requests.get(url + "todos?userId={}".format(param))
    # Transforms JSON data in Python objects
    todos = todos.json()

    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        # "todos" is a list of dicts
        for todo in todos:
            writer.writerow([param, name, todo["completed"], todo["title"]])
