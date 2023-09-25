#!/usr/bin/python3
"""
To export all tasks from all employees
"""

if __name__ == '__main__':

    import json
    import requests

    output = {}
    for i in range(1, 11):
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + "users?id={}".format(i))
        # Transforms JSON data in Python objects
        user = user.json()
        # Gets the name from the user object
        name = user[0]["username"]
        todos = requests.get(url + "todos?userId={}".format(i))
        # Transforms JSON data in Python objects
        todos = todos.json()
        output[i] = []
        for todo in todos:
            output[i].append({"username": name,
                              "task": todo["title"],
                              "completed": todo["completed"]})

    with open("todo_all_employees.json", 'w') as result_file:
        json.dump(output, result_file)
