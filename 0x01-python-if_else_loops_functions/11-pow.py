#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for ans in range(b):
            result *= a
    else:
        for ans in range(-b):
            result /= a
    return result
