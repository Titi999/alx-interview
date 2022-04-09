#!/usr/bin/python3

"""
Module 0-pascal_pascal
"""


def pascal_triangle(n):
    """
    returns a list of integers
    representing Pascal's triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]

    # iterate to up size n - 1
    for i in range(n - 1):
        temp = [0] + pascal[-1] + [0]
        row = []
        for j in range(len(pascal[-1]) + 1):
            # add values to next new row
            row.append(temp[j] + temp[j + 1])
        # add the row to the pascal
        pascal.append(row)
    return pascal
