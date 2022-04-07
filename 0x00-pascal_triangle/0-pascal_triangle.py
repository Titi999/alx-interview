#!/usr/bin/python3
from math import factorial


def pascal_triangle(n):
    p = []
    pascal = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            for j in range(i + 1):
                p.append(factorial(i) // (factorial(j) * factorial(i - j)))
            pascal.append(p)
            p = []
        return pascal
