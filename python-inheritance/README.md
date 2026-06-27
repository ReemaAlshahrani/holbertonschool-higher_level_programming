# Python - Inheritance: Geometry & Shapes

This project explores the concept of **Inheritance** in Python. It demonstrates how to build a scalable class hierarchy, starting from a base geometry class, moving to a specific shape (Rectangle), and finally extending it to a specialized case (Square). It also implements data validation and custom string representations.

---

## Project Tasks & Files Description

| File Name | Class / Function | Description |
| :--- | :--- | :--- |
| `0-lookup.py` | `lookup(obj)` | Returns the list of available attributes and methods of an object. |
| `1-my_list.py` | `MyList` | A class that inherits from `list` and includes a method to print the list sorted. |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` | Returns `True` if the object is exactly an instance of the specified class. |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` | Returns `True` if the object is an instance of, or inherited from, the specified class. |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` | Returns `True` if the object is an instance of a class that inherited (directly/indirectly) from the specified class. |
| `5-base_geometry.py` | `BaseGeometry` | An empty class that serves as the foundation for geometry features. |
| `6-base_geometry.py` | `BaseGeometry` | Improves the base class by adding an unimplemented `area()` method that raises an Exception. |
| `7-base_geometry.py` | `BaseGeometry` | Adds the `integer_validator` method to validate that inputs are positive integers. |
| `8-rectangle.py` | `Rectangle` | Inherits from `BaseGeometry`. Validates and instantiates `width` and `height` using the base validator. |
| `9-rectangle.py` | `Rectangle` | Implements the full `area()` method and customizes the `__str__` method for the rectangle description. |
| `10-square.py` | `Square` | Inherits from `Rectangle`. Instantiates a square with a validated `size` using `super()`. |
| `11-square.py` | `Square` | Advanced square class with a private `size` attribute and a specialized `__str__` custom print description. |

---

## Key Features Implemented

*   **Object-Oriented Programming (OOP):** Deep dive into Single and Multi-level Inheritance.
*   **Data Validation:** Using a centralized validator to ensure all dimensions are strictly positive integers.
*   **Method Overriding:** Customizing the `__str__` magic method to provide readable descriptions for each shape.
*   **Code Reusability:** Leveraging `super().__init__()` to reuse the rectangle's logic inside the square.
