#!/usr/bin/python3
""" defines a private instance attribute """


class Square:
    """ defines a private instance attribute """

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise ValueError("size must be an integer")
        if (size < 0):
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
