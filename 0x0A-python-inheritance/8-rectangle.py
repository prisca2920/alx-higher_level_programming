#!/usr/bin/python3
""" inherits from a class"""


class BaseGeometry:
    """ inherits from a class"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ the new child class """
    def __init__(self, width, height):
        super().__init__
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
