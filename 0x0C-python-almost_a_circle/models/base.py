#!/usr/bin/python3
"""creating class base"""


class Base:
    """creating class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing the class"""
        if id is not None:
            self.id = id
        else:
            Base__nb_objects += 1
            self.id = Base.__nb_objects
