#!/usr/bin/python3
"""Defines a module containing the Square class."""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the new square.
        """
        self.__size = size
