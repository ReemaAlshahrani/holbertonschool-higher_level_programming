#!/usr/bin/python3
"""
Prints an integer safely and outputs errors to stderr.
"""
import sys


def safe_print_integer_err(value):
    """Prints an integer and handles errors by writing to stderr."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
