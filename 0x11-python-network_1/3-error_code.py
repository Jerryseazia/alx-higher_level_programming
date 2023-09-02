#!/usr/bin/python3
"""
manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
given URL & email as params, display response body utf-8, print error codes
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
