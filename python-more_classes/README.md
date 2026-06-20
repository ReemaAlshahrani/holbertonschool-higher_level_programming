# Python - More Classes and Objects

This project is part of the Higher Level Programming curriculum. It covers advanced Object-Oriented Programming (OOP) concepts in Python, including private attributes, getters and setters (properties), class attributes, static methods, class methods, and special magic methods (`__str__`, `__repr__`, `__del__`).

## Technologies
* Language: Python 3.8.5
* OS: Ubuntu 20.04 LTS
* Style Guide: `pycodestyle` (version 2.7.*)

## Learning Objectives
* What is Object-Oriented Programming (OOP)
* The difference between a Class and an Instance
* How to use public, protected, and private attributes
* Understanding `self` and how Python finds attributes
* Implementing getters and setters the Pythonic way using `@property`
* The difference between `__str__` and `__repr__`
* What is a class attribute vs an object attribute
* When to use `@classmethod` and `@staticmethod`

## Files & Tasks

| File | Description |
| --- | --- |
| `0-rectangle.py` | An empty class `Rectangle` that defines a rectangle. |
| `1-rectangle.py` | A class `Rectangle` with private attributes `width` and `height`, including data validation using properties. |
| `2-rectangle.py` | Extends `1-rectangle.py` by adding public instance methods `area()` and `perimeter()`. |
| `3-rectangle.py` | Extends `2-rectangle.py` by adding a custom `__str__` method to print the rectangle using `#`. |
| `4-rectangle.py` | Extends `3-rectangle.py` by adding a custom `__repr__` method to recreate a new instance using `eval()`. |
| `5-rectangle.py` | Extends `4-rectangle.py` by adding a `__del__` method that prints a message when an instance is deleted. |
| `6-rectangle.py` | Extends `5-rectangle.py` by adding a public class attribute `number_of_instances` to track active instances. |
| `7-rectangle.py` | Extends `6-rectangle.py` by adding a public class attribute `print_symbol` to customize the rectangle's string representation. |
| `8-rectangle.py` | Extends `7-rectangle.py` by adding a static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles based on area. |
| `9-rectangle.py` | Extends `8-rectangle.py` by adding a class method `square(cls, size=0)` that acts as a factory method to create a square. |

## Requirements & Usage
* All files are executable and start with `#!/usr/bin/python3`.
* To check the code style, run:
```bash
pycodestyle filename.py
