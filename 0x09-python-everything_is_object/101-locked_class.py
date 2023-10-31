#!/usr/bin/python3
"""creating a locked class"""


class LockedClass:
    """creating a locked class"""
    def __init__(self, first_name):
        if not first_name:
            raise Exception
        self.name = first_name
