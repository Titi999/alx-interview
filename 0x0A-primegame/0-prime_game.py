#!/usr/bin/python3
"""
 Maria and Ben are playing a game.
 Given a set of consecutive integers starting from 1 up to and including n,
 they take turns choosing a prime number from the set and removing that number and its multiples from the set.
 The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    filters = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not filters[i]:
            continue
        for j in range(i * i, n + 1, i):
            filters[j] = False
    filters[0] = filters[1] = False
    c = 0
    for i in range(len(filters)):
        if filters[i]:
            c += 1
        filters[i] = c
    plyr1 = 0
    for n in nums:
        plyr1 += filters[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
