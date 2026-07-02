#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file and returns chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
