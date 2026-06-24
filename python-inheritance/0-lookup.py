#!/usr/bin/python3
"""
This module provides a lookup function for objects.
"""


def lookup(obj):
    """
    A function that returns the list of available
    attributes and methods of an object.
    """
    return dir(obj)
