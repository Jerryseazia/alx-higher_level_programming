#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
given URL & email as params, send POST req to URL, display response body utf-8
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
