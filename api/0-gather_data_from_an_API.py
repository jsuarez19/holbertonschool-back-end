#!/usr/bin/python3
"""
To retrieve data from an API
"""

if __name__ == '__main__':

    import requests
    from sys import argv

    domain = "https://jsonplaceholder.typicode.com"
    param = argv[1]
    user = requests.get(domain + "users?id={}".format(param))
    todos = requests.get(domain + "todos?userId={}".format(param))
    done = requests.get(domain + "todos?userId={}&completed=true".format(param))
    done_list = []

    print("Employee {} is done with tasks({}/{}):"
          .format(user, len(done), todos))

    #n is a dictionary and title is the key
    for n in todos:
        done_list.append("\t {}".format(n["title"]))
    for task in done_list:
        print(task)


 