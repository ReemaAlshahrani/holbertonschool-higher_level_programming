#!/usr/bin/python3
"""
Prints an integer with {:d}.format().
"""


def safe_print_integer(value):
    """Prints an integer safely."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
