#!/usr/bin/python3
""" if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """ if the object is exactly an instance"""
    if type(obj) == a_class:
        return True
    return False
