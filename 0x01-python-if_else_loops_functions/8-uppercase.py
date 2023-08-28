#!/usr/bin/python3
def uppercase(str):
    for val in str:
        uppercase_char = chr(ord(val) - 32) if 'a' <= val <= 'z' else val
        print(uppercase_char, end='')
    print()
