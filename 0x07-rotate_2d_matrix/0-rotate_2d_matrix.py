#!/usr/bin/python3
"""Rotate 2D matrix, 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function

    Args:
        matrix (list): 2D matrix to rotate
    """
    reversed_matrix = zip(*matrix[::-1])
    for n, o in enumerate(reversed_matrix):
        matrix[n] = list(o)
