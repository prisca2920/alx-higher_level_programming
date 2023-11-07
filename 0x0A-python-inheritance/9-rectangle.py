#!/usr/bin/python3
"""creates a class rect from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a class rect from base geometry"""
    def __init__(self, width, height):
        """instantiates width and height"""
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        """returns area of a rect"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string representation"""
        rect = "[" + str(self.__class__.__name__) + "] "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect
