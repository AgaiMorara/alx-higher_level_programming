#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is not None):
        x = len(my_list) - 1
        while (x >= 0):
            print("{:d}".format(my_list[x]))
            x -= 1
