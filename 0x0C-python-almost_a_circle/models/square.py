#!/usr/bin/python3
"""class square that inherits from rect"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """new class square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns str rep of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """defines size of square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """deals with arguments and key value"""
        if args and len(args) != 0:
            the_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, the_args[i], args[i])

        else:
            for key, value in kwargs.items():
                seattr(self, key, value)

    def to_dictionary(self):
        """updates the dict rep of sq"""

        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
