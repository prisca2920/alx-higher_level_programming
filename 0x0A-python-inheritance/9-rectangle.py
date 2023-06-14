#!/usr/bin/python3
""" inherits from a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ the new child class """
    def __init__(self, width, height):
        super().__init__
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}" .format(self.__width, self.__height)
