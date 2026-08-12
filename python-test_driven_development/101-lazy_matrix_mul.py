#!/usr/bin/python3
"""
Module that multiplies 2 matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a (list of lists): The first matrix (int or float).
        m_b (list of lists): The second matrix (int or float).

    Returns:
        ndarray: The matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
