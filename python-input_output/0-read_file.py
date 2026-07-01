#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
