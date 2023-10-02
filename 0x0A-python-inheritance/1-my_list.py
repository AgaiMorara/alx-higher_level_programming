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
        cloned = self[:]
        n = len(cloned)
        changed = True

        while changed:
            changed = False
            for i in range(1, n):
                if cloned[i - 1] > cloned[i]:
                    cloned[i - 1], cloned[i] = cloned[i], cloned[i - 1]
                    swapped = True
                if not changed:
                    break
        return cloned
