#!/usr/bin/python3
"""Module for lazy_matrix_mul function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using NumPy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        The matrix multiplication result.
    """
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("m_b must be a list")

    return np.matmul(m_a, m_b)
