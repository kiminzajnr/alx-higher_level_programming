#!/usr/bin/python3
"""
    divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        forms a new matrix after all elements are divided
    """

    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        transpose = []
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            elem = round(elem / div, 2)
            transpose.append(elem)
        new_matrix.append(transpose)
    return new_matrix
