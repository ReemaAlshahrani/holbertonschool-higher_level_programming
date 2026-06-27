"""Module for learning Duck Typing and Abstract Base Classes in Python."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.radius * self.radius * pi

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return self.radius * 2 * pi


class Rectangle(Shape):
    """Concrete class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return (self.height + self.width) * 2


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
