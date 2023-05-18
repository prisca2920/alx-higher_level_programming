#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for values in new_matrix:
        return list(map(lambda i: i*i, values))
    
