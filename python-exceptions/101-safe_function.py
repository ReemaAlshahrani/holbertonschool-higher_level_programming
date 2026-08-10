#!/usr/bin/python3
"""
Executes a function safely and handles exceptions.
"""
import sys


def safe_function(fct, *args):
    """Executes a function and returns its result or None if an error occurs."""
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
