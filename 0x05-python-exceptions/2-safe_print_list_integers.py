#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    index = 0
    while printed < x:
        try:
            print("{:d}".format(my_list[index]), end='')
            printed += 1
        except (ValueError, TypeError):
            pass
        index += 1
    print()
    return printed
