#!/usr/bin/python3
"""
Module contains function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place
    """
    if len(matrix) < 2:
        return

    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
