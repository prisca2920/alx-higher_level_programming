#!/usr/bin/python3
"""creates a class rect from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a class rect from base geometry"""
    def __init__(self, width, height):
        """instantiates width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
