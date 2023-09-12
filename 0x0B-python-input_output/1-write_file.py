#!/usr/bin/python3
"""
attribute write... of stream object... writes to a file
"""


def write_file(filename="", text=""):
    """ writes in utf8...specification of encoding is important because
    defauls in different operating systems are different
    """

    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
        return (count)
