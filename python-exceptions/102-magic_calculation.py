#!/usr/bin/python3
"""
Function that performs a calculation based on Python bytecode.
"""


def magic_calculation(a, b):
    """Replicates a specific computation defined by Python bytecode."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
