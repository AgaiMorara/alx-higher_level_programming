#!/usr/bin/python3
"""
Module to divided two matrixes elementwise
"""


def matrix_divided(matrix, div):
    """ implements elelentwise division of the matrix
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list)
               and all(isinstance(x, (int, float))
                       for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
