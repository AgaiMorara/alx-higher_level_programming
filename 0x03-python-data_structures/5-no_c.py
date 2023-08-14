#!/usr/bin/python3
def no_c(my_string):
    answer = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            answer += char
    return answer
