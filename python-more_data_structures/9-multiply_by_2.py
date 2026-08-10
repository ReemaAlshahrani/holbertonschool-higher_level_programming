#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    # Create a new dictionary with values multiplied by 2 using dict comprehension
    return {key: value * 2 for key, value in a_dictionary.items()}
