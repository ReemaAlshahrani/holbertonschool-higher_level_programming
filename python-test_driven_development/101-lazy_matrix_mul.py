#!/usr/bin/python3
"""
Module that multiplies 2 matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.
    """
    return np.matmul(m_a, m_b)
