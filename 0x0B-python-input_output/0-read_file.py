#!/usr/bin/python3
"""a func that reads a text file"""


def read_file(filename=""):
    """a func that reads a text file"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
