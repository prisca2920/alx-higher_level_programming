#!/usr/bin/python3
""" a class MyList that inherits from list"""


class Mylist(list):
    """inherits from list"""
    def print_sorted(self):
        """printing a sorted list"""
        print(sorted(self))
