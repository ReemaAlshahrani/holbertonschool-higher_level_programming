# Python - Abstract Base Classes (ABC) & Advanced OOP Concepts

This project explores advanced Object-Oriented Programming (OOP) concepts in Python, focusing on structural design, inheritance models, and code reusability. Through a series of practical tasks, it demonstrates Abstract Base Classes (ABCs), Duck Typing, Subclassing built-in types, Multiple Inheritance, and Mixins.

## Project Structure & Concept Overview

The following table provides a quick guide to the files included in this project, the core programming concepts they illustrate, and their structural behaviors:

| File Name | OOP Concept | Description & Key Functionality |
| :--- | :--- | :--- |
| **`task_00_abstract_class_shape.py`** | Abstract Base Classes | Defines a strict blueprint class `Shape` (`abc.ABC`) enforcing `area()` and `perimeter()` interfaces on subclasses like `Circle` and `Rectangle`. |
| **`task_01_duck_typing.py`** | Duck Typing & Polymorphism | Implements dynamic polymorphism via `shape_info(shape)`, evaluating objects based on their available methods rather than their strict class type. |
| **`task_02_verboselist.py`** | Extending Built-in Types | Customizes the native `list` class into `VerboseList`, intercepting mutation methods (`append`, `extend`, etc.) using `super()` to trigger live notifications. |
| **`task_03_countediterator.py`** | Iteration Protocols | Wraps standard iterables into a `CountedIterator` that overrides the `__next__` method to monitor and count how many items have been processed. |
| **`task_04_flyingfish.py`** | Multiple Inheritance & MRO | Explores multiple class derivation with `FlyingFish` inheriting from `Fish` and `Bird`, demonstrating how Python handles overlapping methods via C3 Linearization (MRO). |
| **`task_05_dragon.py`** | Modular Mixins Pattern | Composes a `Dragon` class by blending highly focused, reusable feature mixins (`SwimMixin` and `FlyMixin`) instead of creating deep, rigid inheritance structures. |

## Setup & Testing

To execute any of the test main files provided within this module, run:

```bash
python3 main_01_duck_typing.py
python3 main_02_verboselist.py
python3 main_03_countediterator.py
python3 main_04_flyingfish.py
python3 main_05_dragon.py
