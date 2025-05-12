#!/usr/bin/python3

def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    max_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[max_key]

    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            max_key = k
    return (max_key)
