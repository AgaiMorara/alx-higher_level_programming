#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        up = "{:c}".format(ord(char) - 32) if 'a' <= char <= 'z' else char
        result += up
    print(result)
