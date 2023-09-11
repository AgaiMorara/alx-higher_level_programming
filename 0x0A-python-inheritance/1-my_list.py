#!/usr/bin/python3
'''
a class Mylist that inherits from list defined previously
'''


class MyList(list):
    """
    args:
    list - the base class, my list is the subclass
    prints the list , but sorted
    """
    def print_sorted(self):
        ''' sorts and prints the list using bubble sort'''
        print(sorted(self))
