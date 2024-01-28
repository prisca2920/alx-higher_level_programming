#!/usr/bin/python3
"""fetches a url"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://alx-intranet.hbtn.io/status") as f:
        fi = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(fi)))
        print("\t- content: {}".format(fi))
        print("\t- utf8 content: {}".format(fi.decode(encoding='utf-8')))
