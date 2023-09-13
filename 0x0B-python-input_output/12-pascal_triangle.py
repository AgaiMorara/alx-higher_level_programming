#!/usr/bin/python3
"""
Pascal_triangle: to return a list of lists of integers representing the
Pascals triangle of n
"""


def pascal_triangle(n):
    """ The trick to the pascal triangle are patterns to its symmetry... We
    will always start with one and end with one...for the middle elements
    we will use the previous list add the element at
    the ith position and one at i- 1 position to find the current position
    """
    if n < 1:
        return []
    result = [[1]]
    for i in range(1, n):
        pascal = [1]
        prev = result[-1]

        for j in range(len(prev) - 1):
            ans = prev[j] + prev[j + 1]
            pascal.append(ans)
        pascal.append(1)
        result.append(pascal)
    return result
