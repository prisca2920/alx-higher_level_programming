#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        texts = f.write(text)
        print(texts)
