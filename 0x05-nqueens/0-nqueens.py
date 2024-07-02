#!/usr/bin/python3

"""
Contains solution to nqueens problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def n_queens(n, i=0, a=[], b=[], c=[]):
    """
    Finds all the possible positions of the queen
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from n_queens(
                    n,
                    i + 1,
                    a + [j],
                    b + [i + j],
                    c + [i - j]
                    )
    else:
        yield a


def solve_nqueens(n):
    """
    Solves and prints all placement combinations
    """
    k = []
    i = 0

    for position in n_queens(n, 0):
        for pos in position:
            k.append([i, pos])
            i += 1
        print(k)
        k = []
        i = 0


solve_nqueens(n)
