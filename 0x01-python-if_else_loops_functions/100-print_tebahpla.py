#!/usr/bin/python3

for val in range(122, 96, -1):
    print("{}".format(chr(val).upper() if val % 2 == 1 else chr(val)), end='')
