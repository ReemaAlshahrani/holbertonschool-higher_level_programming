#!/usr/bin/python3
"""
Module that provides an integer addition function.

Contains add_integer function which handles integers,
floats casting, and raises appropriate TypeErrors.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after casting floats to integers.
    Raises TypeError if inputs are not int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
