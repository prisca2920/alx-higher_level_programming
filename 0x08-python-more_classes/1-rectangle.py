#!/usr/bin/python3
""" defining class rectangle"""


class Rectangle:
    """defining class rects"""
    def __init__(self, width=0, height=0):
        """initializing class rect"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of a rect"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a rect"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """gets the height of a rect"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rect"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
