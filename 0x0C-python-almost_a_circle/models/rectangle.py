#!/usr/bin/python3
"""creating a class rect"""


class Rectangle(Base):
    """creating a class rect"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """defining the getter method"""
            return self.__width

        @property
        def height(self):
            """defining the getter method"""
            return self.__height

        @property
        def x(self):
            """defining the getter method"""
            return self.__x

        @property
        def y(self):
            """defining the getter method"""
            return self.__y

        @width.setter
        def width(self, value):
            """setting the width of the rect"""
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value <= 0:
                raise VlueError('width must be > 0')
            self.__width = value

        @height.setter
        def height(self, value):
            """setting the height of the rect"""
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value

        @y.setter
        def y(self, value):
            """setting the y of the rect"""
            if not isinstance(value, int):
                raise TypeError('y must be an integer')
            if value <= 0:
                raise ValueError('y must be > 0')
            self.__y = value

        @x.setter
        def x(self, value):
            """setting the x of the rect"""
            if not isinstance(value, int):
                raise TypeError('x must be an integer')
            if value <= 0:
                raise ValueError('x must be > 0')
            self.__x = value

        def area(self):
            """returns the area value of the rect"""
            return self.__height * self.__width

        def display(self):
            """displays # character of rect in stdout"""
