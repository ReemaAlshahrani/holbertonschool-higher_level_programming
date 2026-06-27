#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
