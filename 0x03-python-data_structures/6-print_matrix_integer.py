#!/usr/bin/python3
""" prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    """ this function prints a matrix of integers"""
    if matrix != [[]]:
        for row in matrix:
            for elem in row:
                print("{:d}".format(elem), end=" "
                      if elem != row[-1] else '\n')
    else:
        print()
