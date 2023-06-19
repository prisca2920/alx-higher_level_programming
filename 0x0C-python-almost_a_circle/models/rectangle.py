#!/usr/bin/python3
""" new class retangle"""
from models.base import Base


class Rectangle(Base):
    """new class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """gets width of rect"""
            return self.__width

        @width.setter
        """sets the width"""
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        """gets height of rect"""
        def height(self):
            return self.__height

        @height.setter
        """sets how to retrieve height"""
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """returns the x coordinates of a rect"""
            return self.__x

        @x.setter
        """sets how to retrieve it"""
        def x(self, value):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        """returns y coordinates of a rect"""
        def y(self):
            return self.__y

        @y.setter
        """sets how to retrieve it"""
        def y(self, value):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """defines the area of a rect"""
            return self.__width * self.__height

        def display(self):
            """draws a rect using #"""
            for y in range(self.y):
                print("")
            for i in range(self.__height):
                for x in range(self.x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

