#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    if isinstance(roman_string, str):

        for char in roman_string:
            current_value = roman_to_int_map[char]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

    return total
