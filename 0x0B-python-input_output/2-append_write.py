#!/usr/bin/python3
"""that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
       lines =  f.write(text)
       return lines
