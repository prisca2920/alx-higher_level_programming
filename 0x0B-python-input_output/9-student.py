#!/usr/bin/python3
""" creating a class student"""


class Student:
    """ creating a class student"""
    def __init__(self, first_name, last_name, age):
        """initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict rep"""
        return self.__dict__
