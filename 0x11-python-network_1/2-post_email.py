#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    email = urlencode(value).encode('ascii')
    request = urllib.request.Request(url, email)
    with urllib.request.urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
