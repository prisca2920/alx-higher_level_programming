#!/usr/bin/python3
""" returns an instance before deleting a rectangle """


class Rectangle:
    """ returns an instance before deleting a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """gives the reader a visual representation """

        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            r = []
            for i in range(self.__height):
                [r.append(str(self.print_symbol)) for j in range(self.__width)]
                if i != self.__height - 1:
                    r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """ draws a string rep """

        return "Rectangle({}, {})" .format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger triangle """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2

    def __del__(self):
        """deletes a rectangle """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
