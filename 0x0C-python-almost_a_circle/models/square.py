#!/usr/bin/python3
"""creating a class sq"""


class Square(Rectangle):
    """creating a class sq"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the class"""
        super().__init__(id, x, y, size, size)
        self.width = size
        self.height = size

    def __str__(self):
        """returns the str representation"""
        return f"[Square] ({self.__id}) {self.__x}/{self.__y} - {self.__size}"

    @property
    def size(self):
        """returns the size of sq"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the value of sq"""
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updating args and key word arguments"""
        if args != None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attrs[i] == 'size'
                setattr(self, 'width', args[i])
                setattr(self, 'height', args[i])
            else:
                setattr(self, attr[i], args[i])

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
