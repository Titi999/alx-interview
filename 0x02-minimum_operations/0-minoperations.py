#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest
number of operations needed to result in exactly n H characters
in the file.
"""


def factorize(n):
    """ returns the sum of prime factors of n or n if n is prime"""
    initial = 2
    prime_sum = 0
    while initial <= n:
        if n % initial == 0:
            n = n // initial
            prime_sum += initial
            initial -= 1
        initial += 1
    return prime_sum


def minOperations(n):
    """
    returns the fewest number of needed operations or 0 if impossible
    """
    if not isinstance(n, int) or n < 2:
        return 0
    return factorize(n)
