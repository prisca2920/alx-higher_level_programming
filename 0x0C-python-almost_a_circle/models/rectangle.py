#!/usr/bin/python3
"""creating a class rect"""
from models.base import Base


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
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise VlueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """setting the height of the rect"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @y.setter
    def y(self, value):
        """setting the y of the rect"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value <= 0:
            raise ValueError('y must be > 0')
        self.__y = value

    @x.setter
    def x(self, value):
        """setting the x of the rect"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value <= 0:
            raise ValueError('x must be > 0')
        self.__x = value

    def area(self):
        """returns the area value of the rect"""
        return self.__height * self.__width

    def display(self):
        """displays # character of rect in stdout"""
        for y in range(self.y):
            print('')
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """returns a string representation"""
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} - \
                {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns args to each attr"""
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict representation of rect"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        dict1 = {}

        for key in attrs:
            dict1[key] = getattr(self, key)

        return dict1
