#!/usr/bin/python3
""" defines a square by size"""


class Square:
    """ defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the class square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """defines the size property of a sq"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of  sq using value"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        """ returns the coordinates of a sq"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the coordinates of the sq"""
        self.__position = value
        if value < 0 and len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout # sq representation"""
        for i in range(self.__size):
            if self.__position[1] > 0:
                print(' ' * self.position[1], end="")
            print('#' * self.__size)
        if self.__size == 0:
            print('')
