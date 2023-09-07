#!/bin/usr/python3
"""Defines a matrix division function"""

def matrix_divided(matrix, div):
    """
        Divide all element of a matrix.
    """
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("Div must be a number")
    if div == 0:
          raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        transpose = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("Matrix must be a(list of lists)\
of integers/float")
            elem = round(elem / div, 2)
            transpose.append(elem)
        new_matrix.append(transpose)

    return new_matrix
