#!/usr/bin/python3
"""if an obj is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """if an obj is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
