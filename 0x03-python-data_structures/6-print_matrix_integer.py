#!/usr/bin/python3
""" prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    """ this function prints a matrix of integers"""
    for row in matrix:
        for elem in row:
            print(" {:d}".format(elem), end="")
        print()
