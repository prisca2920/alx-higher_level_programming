#!/usr/bin/python3
"""inherited from a class """


def inherits_from(obj, a_class):
    """inherited from a class """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
