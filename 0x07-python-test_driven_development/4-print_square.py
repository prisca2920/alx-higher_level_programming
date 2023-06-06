#!/usr/bin/python3
""" draws a # square """


def print_square(size):
    """ draws a # square """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return 0
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
