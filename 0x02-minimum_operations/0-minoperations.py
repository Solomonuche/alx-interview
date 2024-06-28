#!/usr/bin/python3
"""
Function that calculates the min operations to copy and
paste letters
"""


def minOperations(n):
    ops = 0
    minOps = 2
    while n > 1:
        while n % minOps == 0:
            ops += minOps
            n /= minOps
        minOps += 1
    return ops
