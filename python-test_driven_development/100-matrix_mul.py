#!/usr/bin/python3
"""
Module that provides a function to multiply 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, list of lists,
                   contains non-int/float, or rows are not same size.
        ValueError: If m_a or m_b is empty or cannot be multiplied.
    """
    # 1. Validate if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validate if m_a and m_b are list of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # 3. Validate if m_a or m_b is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validate elements in m_a and m_b are integers or floats
    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Validate that m_a and m_b are rectangles
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 6. Validate if m_a and m_b can be multiplied
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row_result.append(total)
        result.append(row_result)

    return result
