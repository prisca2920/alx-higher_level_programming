#!/usr/bin/python3
"""defines a node of a singly linked list"""

class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the class node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns attr data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of data"""
        self.__data = value
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """returns the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next node value"""
        self.__next_node = value
        if not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    """new class singly linked list"""
    def __init__(self):
        """initializes the class"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts new node in correct position"""
