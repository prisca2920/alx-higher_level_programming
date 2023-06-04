#!/usr/bin/python3
""" divides elements of a matrix """


def matrix_divided(matrix, div):
    """ divides elements of a matrix """

    if type(matrix[]) is not int or float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div)O is not int or float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    else:
        for i in matrix:
            return div / i
