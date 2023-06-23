#!/usr/bin/python3
"""new class retangle"""
from models.base import Base


class Rectangle(Base):
    """new class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width of rect"""
        return self.__width

    @property
    def height(self):
        """Gets height of rect"""
        return self.__height

    @property
    def x(self):
        """Gets x value of rect"""
        return self.__x

    @property
    def y(self):
        """Gets y value of rect"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width of rect"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height of rect"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x value of rect"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y value of rect"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for i in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """updates the str methof of rect"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """support args and keyword args"""
        if args and len(args) != 0:
            the_args = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, the_args[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        return {'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }
