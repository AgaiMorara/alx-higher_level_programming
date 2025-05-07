#!/usr/bin/python3
def max_integer(my_list=[]):
    big = None
    if my_list:
        big = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > big:
                big = my_list[i]
    return (big)
