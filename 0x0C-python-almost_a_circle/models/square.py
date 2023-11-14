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
        if args is not None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attrs[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attrs[i], args[i])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict rep of sq"""
        atrs = ['id', 'size', 'x', 'y']
        dict2 = {}

        for key in attrs:
            if key == 'size':
                dict2[key] = getattr(self, key)
            else:
                dict2 = getattr(self, key)

        return dict2
