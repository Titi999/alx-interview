#!/usr/bin/python3
"""
A function to rotate n X n matrix
It should not return anything
"""


def rotate_2d_matrix(matrix):
    rotate = []
    for i in range(0, len(matrix)):
        rotate.append([j[i] for j in reversed(matrix)])
    matrix.clear()
    matrix += rotate
