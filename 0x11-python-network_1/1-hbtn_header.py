#!/usr/bin/python3
"""sends a request and displays value"""
from sys import argv
from urllib import request


if __name__ == '__main__':
    with request.urlopen(request.Request(argv[1])) as f:
        print(dict(f.headers).get("X-Request-Id"))
