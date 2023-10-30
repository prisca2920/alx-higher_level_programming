#!/usr/bin/python3
""" defining class rectangle"""


class Rectangle:
    """defining class rects"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializing class rect"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the area of a rect"""
        return self.__width * self.__height

    def perimeter(self):
        """finds the perimeter of a rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the str rep of rect"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """str rep of rect to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rect"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rect instance"""
        return (cls(size, size))

    def __del__(self):
        """deletes an instance rect"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
