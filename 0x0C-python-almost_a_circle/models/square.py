#!/usr/bin/python3
"""creating a class sq"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating a class sq"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns the str representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """returns the size of sq"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the value of sq"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updating args and key word arguments"""
        attrs = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict rep of sq"""
        attrs = ['id', 'size', 'x', 'y']
        dict2 = {}

        for key in attrs:
            if key == 'size':
                dict2[key] = getattr(self, 'width')
            else:
                dict2[key] = getattr(self, key)

        return dict2
