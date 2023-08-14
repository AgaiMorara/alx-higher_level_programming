#!/usr/bin/python3
def print_last_digit(number):
    absnumb = number if number >= 0 else number * -1
    print(absnumb % 10, end='')
    return(absnumb % 10)
