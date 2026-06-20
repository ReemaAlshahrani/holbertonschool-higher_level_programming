#!/usr/bin/python3
"""Defines a module containing the Square class."""


class Square:
    """Defines a square with a private size attribute and validation."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
