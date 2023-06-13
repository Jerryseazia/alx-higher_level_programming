#!/usr/bin/python3
"""
Script reads stdin line by line and computes metrics

prints those statistics since the beginning:
total file size and
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

format: File size: <total size>
format: <status code (in ascending order)>: <number>
"""


import sys


def print_size_and_codes(size, stat_codes):
    print("File size: {:d}".format(size))
    for c, d in sorted(stat_codes.items()):
        if d:
            print("{:s}: {:d}".format(c, d))


def parse_stdin_and_compute():
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise

    print_size_and_codes(size, stat_codes)


parse_stdin_and_compute()
