#!/usr/bin/python3
"""
A function that prints a text with 2 new lines after each {., ?, and : }
occurence
"""

def text_indentation(text):
    """check wether text is a string """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """initialize empty string in which we will write text"""
    forprint = ""

    for l in text:
        forprint += l
        if l in ".?:":
            forprint += "\n\n"
    """ strip each whitespace at the beginning or end of line """
    sentences = [sentence.strip() for sentence in forprint.splitlines()]
    new_text = "\n".join(sentences)
    print(new_text)
