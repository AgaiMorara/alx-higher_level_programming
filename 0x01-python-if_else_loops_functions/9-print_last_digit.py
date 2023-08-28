#!/usr/bin/python3
def print_last_digit(number):
    absnumb = number if number >= 0 else number * -1
    last_digit = absnumb % 10
    print("{}".format(last_digit), end='')
    return last_digit
