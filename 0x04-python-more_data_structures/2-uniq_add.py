#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    return sum([unique_integers.add(num) or num for num in
                my_list if num not in unique_integers])
