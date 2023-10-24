#!/usr/bin/python3
""" defines a square by size"""


class Square:
    """ defines a square by size"""
    def __init__(self, size=0):
        """initializes the class square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size
