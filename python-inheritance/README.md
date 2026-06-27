# Python - Inheritance: Geometry & Shapes

This project explores the concept of **Inheritance** in Python. It demonstrates how to build a scalable class hierarchy, starting from a base geometry class, moving to a specific shape (Rectangle), and finally extending it to a specialized case (Square). It also implements data validation and custom string representations.

---

##  Files Description

| File Name | Class | Description |
| :--- | :--- | :--- |
| `7-base_geometry.py` | `BaseGeometry` | The base class containing data validation mechanism (`integer_validator`) to ensure inputs are positive integers. |
| `9-rectangle.py` | `Rectangle` | Inherits from `BaseGeometry`. It validates and stores `width` and `height`, implements the `area()` method, and customizes printing. |
| `11-square.py` | `Square` | Inherits from `Rectangle`. It represents a square with a private `size`, reuse validation, and provides a distinct string representation. |

---

##  Key Features Implemented

*   **Object-Oriented Programming (OOP):** Deep dive into Single and Multi-level Inheritance.
*   **Data Validation:** Using a centralized validator to ensure all dimensions are strictly positive integers.
*   **Method Overriding:** Customizing the `__str__` magic method to provide readable descriptions for each shape.
*   **Code Reusability:** Leveraging `super().__init__()` to reuse the rectangle's logic inside the square.
