#!/usr/bin/python3
"""creating class base"""


class Base:
    """creating class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing the class"""
        if id != None:
            self.id = id
        __nb_objects = id
        __nb_objects += 1
