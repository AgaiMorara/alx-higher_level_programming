#!/usr/bin/python3
import sys


def comline():
    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("0 arguments.")
    else:
        print("{:d} argument(s):".format(n))
        for i, arg in enumerate(argv, start=1):
            print("{:d}: {}".format(i, arg))


if __name__ == "__main__":
    comline()
