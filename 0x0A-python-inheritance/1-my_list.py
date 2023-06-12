#!/usr/bin/python3
""" an inherince of a list"""


class Mylist(list):
    """ an inheritance of a list"""
    def print_sorted(self):
        print(sorted(self))
