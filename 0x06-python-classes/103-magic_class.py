#!/usr/bin/python3
"""creates a magic class"""
import math


class MagicClass:
    """creates a magic class"""

    def __init__(self, radius=None):
        """initializes the radius"""
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """defines the area of a circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """defines the circumference of a circle"""
        return (2 * math.pi * self.__radius)
