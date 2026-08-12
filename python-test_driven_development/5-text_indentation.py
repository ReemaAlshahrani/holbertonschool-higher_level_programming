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

    # Remove trailing spaces from the end of the entire string
    text = text.strip(" ")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            print(char, end="")
            if char in ".?:":
                print("\n")
                flag = 0
