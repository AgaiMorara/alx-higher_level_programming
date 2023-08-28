#!/usr/bin/python3

def safe_print_integer_err(value):

    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except Exception as V:
        print("Exception: {}".format(V), file=stderr, flush=True)
        return False
