#!/usr/bin/python3
"""
Really hard... Reads stdin line by line and computes metrics
"""
import sys


def  print_stats(size, codes):
    """ prints the stats when invoked.
    Args:
        size: we use number of bytes to determine size
        codes: sum of codes
    """

    print("{}: {}".format(key, codes[key]))

    count = 0
    size = 0
    codes = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


    try:
        for line in sys.stdin:
            count = 1 if count == 10 else count + 1
        line = line.split()
        try:
            size += 
