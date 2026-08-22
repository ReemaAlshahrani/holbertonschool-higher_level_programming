#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """A class that prevents the user from dynamically creating
    new instance attributes, except if the attribute is first_name.
    """
    __slots__ = ["first_name"]
