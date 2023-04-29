#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    username = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
    response = get(url)
    objects = response.json()
    try:
        for i in range(10):
            print('{}: {}'.format(objects[i].get('sha'),
                                  objects[i].get('commit').get('author').
                                  get('name')))
    except Exception:
        pass
