#!/usr/bin/python3
"""sends a post request"""
from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
    email = {"email": argv[2]}
    url = argv[1]
    data = parse.urlencode(email).encode("ascii")
    query = request.Request(url, data)

    with request.urlopen(query) as f:
        print(f.read().decode("utf-8"))
