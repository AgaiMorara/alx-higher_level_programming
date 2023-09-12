#!/usr/bin/python3
"""
attribute write... of stream object... writes to a file.. append this time
"""


def append_write(filename="", text=""):
    """ writes in utf8...specification of encoding is important because
    defauls in different operating systems are different
    """

    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
        return (count)
