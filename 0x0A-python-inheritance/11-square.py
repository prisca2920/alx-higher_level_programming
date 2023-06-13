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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}" .format(self.__width, self.__height)


class Square(Rectangle):
    """ new subclass from rect"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
