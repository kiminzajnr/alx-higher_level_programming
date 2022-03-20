#!/usr/bin/python3
""" compute the square value of all integers of a matrix using map"""


def square_matrix_map(matrix=[]):
    """ return squared matrix"""
    return list(map(lambda x: list(map(lambda y: (y**2), x)), matrix))
