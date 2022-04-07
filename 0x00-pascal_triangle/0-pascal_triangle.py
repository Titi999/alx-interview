#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [0] * n

    for i in range(n):
        new = [0] * (i + 1)
        new[0] = 1
        new[len(new) - 1] = 1

        for j in range(1, i):
            if 0 < j < len(new):
                new[j] = pascal[i - 1][j] + pascal[i - 1][j - 1]

        pascal[i] = new

    return pascal
