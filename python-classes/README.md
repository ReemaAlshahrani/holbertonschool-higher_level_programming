# Python - Classes and Objects

This project is part of the Higher-Level Programming curriculum. It covers the fundamentals of Object-Oriented Programming (OOP) in Python, focusing on classes, attributes, methods, data validation, and encapsulation using getters and setters.

## Technologies
* Python (Version 3.8.5)
* Style guide: `PEP 8` (version 1.7.*)

## Files & Tasks Description

| File | Description |
| --- | --- |
| `0-square.py` | An empty class `Square` that defines a square. |
| `1-square.py` | A class `Square` with a private instance attribute `size`. |
| `2-square.py` | Adds validation to `size` (must be an integer and $\ge 0$). |
| `3-square.py` | Adds a public instance method `area(self)` that returns the current square area. |
| `4-square.py` | Introduces getters and setters (`@property`) to access and update the private `size` attribute safely. |
| `5-square.py` | Adds a public instance method `my_print(self)` that prints the square using the `#` character. |
| `6-square.py` | Introduces a private `position` attribute (tuple of 2 positive integers) to handle square coordinates and adds indentation/spaces to `my_print`. |

## How to Use
You can import the `Square` class from any of these modules to create and interact with square objects. For example, using `6-square.py`:

```python
Square = __import__('6-square').Square

# Create a square of size 3 at position (1, 1)
my_square = Square(3, (1, 1))

# Print its area
print("Area:", my_square.area())

# Print the visual square
my_square.my_print()
