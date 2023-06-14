#!/usr/bin/python3
""" inherits from a class rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ new subclass from rect"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
