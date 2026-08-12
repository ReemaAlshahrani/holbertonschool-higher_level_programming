#!/usr/bin/python3
"""Module for lazy_matrix_mul function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using NumPy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        The matrix multiplication result as a NumPy ndarray.
    """
    try:
        return np.matmul(m_a, m_b)
    except TypeError as e:
        raise TypeError(str(e))
