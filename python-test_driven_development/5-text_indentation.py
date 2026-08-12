#!/usr/bin/python3
"""
Module that provides a function to print text with 2 new lines
after specific delimiter characters (., ?, and :).
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    Leading and trailing spaces are removed from each printed line.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    length = len(text)

    # Skip initial leading spaces
    while c < length and text[c] == ' ':
        c += 1

    while c < length:
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            # Skip spaces immediately following the delimiter
            while c < length and text[c] == ' ':
                c += 1
            continue
        c += 1
