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
        def width(self, value):
            """sets the width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
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
        def x(self, value):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            return self.__width * self.__height

        def display(self):
            for y in range(self.y):
                print("")
            for i in range(self.__height):
                for x in range(self.x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            """updates the str method of a rect"""
            return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

