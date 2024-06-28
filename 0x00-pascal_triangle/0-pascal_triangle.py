#!/usr/bin/python3
"""Module to find Pascal's Triangle integers"""


def pascal_triangle(n):
    """Function to find Pascal's Triangle integers

    n (int): The number of rows of Pascal's Triangle.

    Returns:
        Pascal_triangle (list): Binary string of the sum of a and b

    """
    pascal_triangle = list()

    if n <= 0:
        return pascal_triangle

    # add first 1
    if n > 0:
        pascal_triangle.append([1])

    # add second line
    if n > 1:
        pascal_triangle.append([1, 1])

    for i in range(3, n+1):
        pascal_triangle.append([0] * i)

        # Set first and last 1
        pascal_triangle[i-1][0] = 1
        pascal_triangle[i-1][i-1] = 1

        # Calculate middle numbers
        for j in range(1, i-1):
            pascal_triangle[i-1][j] = \
                pascal_triangle[i-2][j-1] + pascal_triangle[i-2][j]
    return pascal_triangle
