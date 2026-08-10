#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a 2D matrix."""
    # Create a new matrix with squared values without modifying the original
    return [[element ** 2 for element in row] for row in matrix]
