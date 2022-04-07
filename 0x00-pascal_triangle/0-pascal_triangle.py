#!/usr/bin/python3
from math import factorial


def pascal_triangle(n):
    p = []
    pascal = []
    if n > 0:
        for i in range(n):
            for j in range(i+1):
                val = factorial(i)//(factorial(j)*factorial(i-j))
                p.append(val)
            pascal.append(p)
            p = []
        return pascal

    else:
        return n <= 0
