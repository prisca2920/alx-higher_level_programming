#!/usr/bin/python3
"""creating an empty class geometry"""


class BaseGeometry:
    """creating an empty class geometry"""
    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) != int:
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
        self.name = name
        self.value = value
