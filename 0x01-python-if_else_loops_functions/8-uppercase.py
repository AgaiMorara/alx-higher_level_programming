#!/usr/bin/python3
def uppercase(s):
    for val in s:
        uppercase_char = chr(ord(val) - 32) if 'a' <= val <= 'z' else val
        print(uppercase_char, end='')
    print()
