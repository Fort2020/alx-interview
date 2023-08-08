#!/usr/bin/python3
"""a method that calculates the
   fewest number of operations
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
