# Python - Abstract Base Classes (ABC) & Advanced OOP Concepts

This project explores advanced Object-Oriented Programming (OOP) concepts in Python, focusing on structural design, inheritance models, and code reusability. Through a series of practical tasks, it demonstrates Abstract Base Classes (ABCs), Duck Typing, Subclassing built-in types, Multiple Inheritance, and Mixins.

## Project Structure & Files Description

Inside the `python-abc` directory, each file targets a specific concept:

### 1. `task_00_abstract_class_shape.py` - Abstract Base Classes
* **Concept:** Interfaces and Enforced Blueprints.
* **Description:** Defines an abstract class `Shape` using Python's `abc` module with abstract methods `area()` and `perimeter()`. It implements concrete subclasses `Circle` and `Rectangle` that must fulfill this interface contract, handling radius/dimension constraints appropriately.

### 2. `task_01_duck_typing.py` - Duck Typing & Polymorphism
* **Concept:** "If it walks like a duck and quacks like a duck, it's a duck."
* **Description:** Demonstrates dynamic typing polymorphism via a standalone function `shape_info(shape)`. This function interacts with any object that implements `area()` and `perimeter()` methods without explicitly enforcing an inheritance check, emphasizing behavior over rigid class hierarchies.

### 3. `task_02_verboselist.py` - Extending Built-in Classes
* **Concept:** Class Extension and Intercepting Behaviors.
* **Description:** Creates a custom class `VerboseList` that inherits from Python's native `list`. By overriding modification methods (`append`, `extend`, `remove`, `pop`) and utilizing `super()`, it injects real-time custom console notifications whenever elements are added or removed.

### 4. `task_03_countediterator.py` - Custom Iterators
* **Concept:** Iteration Protocols.
* **Description:** Implements `CountedIterator` which wraps around any standard iterable object. It overrides the `__next__` dunder method to monitor and count how many items have been successfully fetched during a loop or manual iteration sequence, gracefully raising `StopIteration` when completed.

### 5. `task_04_flyingfish.py` - Multiple Inheritance & MRO
* **Concept:** Diamond Problems and Method Resolution Order (MRO).
* **Description:** Explores inheriting from multiple parents simultaneously through a `FlyingFish` class that derives from both `Fish` and `Bird`. It highlights how Python resolves overlapping methods (like `habitat`) using the C3 Linearization algorithm (`Class.mro()`).

### 6. `task_05_dragon.py` - Mastering Mixins
* **Concept:** Modular Composition over Deep Inheritance.
* **Description:** Showcases the Mixin design pattern by building discrete, single-purpose classes (`SwimMixin` and `FlyMixin`). These components are mixed into a `Dragon` class, providing modular capabilities in a clean, reusable fashion without locking code into deep hierarchies.

## Setup & Testing

To execute any of the test main files provided within this module, run:

```bash
python3 main_01_duck_typing.py
python3 main_02_verboselist.py
python3 main_03_countediterator.py
python3 main_04_flyingfish.py
python3 main_05_dragon.py
