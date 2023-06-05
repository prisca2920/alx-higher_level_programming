#!/usr/bin/python3
""" adds two integers"""


def add_integer(a, b=98):
    """ adds two integers """

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    else:
        result = 0
        result = int(a) + int(b)
        return result
