#!/usr/bin/python3
"""
To export data in JSON format
"""

if __name__ == '__main__':

    import requests
    from sys import argv

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
    output = {}
    output[param] = []

    for todo in todos:
        output[param].append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": name})
    
    with open("{}.json".format(param), 'w') as result_file:
        json.dump(output, result_file)