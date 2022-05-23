#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    rotate = []
    for i in range(0, len(matrix)):
        rotate.append([j[i] for j in reversed(matrix)])
    matrix.clear()
    matrix += rotate
    return matrix
