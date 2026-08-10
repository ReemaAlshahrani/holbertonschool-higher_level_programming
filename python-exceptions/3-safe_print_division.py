#!/usr/bin/python3
"""
Divides two integers and prints the result inside finally section.
"""


def safe_print_division(a, b):
    """Divides two integers safely and prints result in finally block."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
