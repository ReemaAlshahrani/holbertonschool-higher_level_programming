#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an inherited instance of a_class; otherwise False.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
