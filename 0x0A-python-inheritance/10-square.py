#!/usr/bin/python3
"""creating a class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating class sq inheriting from rect"""
    def __init__(self, size):
        """initializing size"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of a rect"""
        return self.__size ** 2
