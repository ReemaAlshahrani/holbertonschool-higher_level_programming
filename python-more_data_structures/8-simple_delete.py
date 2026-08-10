#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary if it exists."""
    # Check if key exists in dictionary before deleting
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
