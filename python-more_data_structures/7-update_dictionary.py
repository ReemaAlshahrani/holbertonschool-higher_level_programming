#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds a key/value pair in a dictionary."""
    # Update the value if key exists, or create it if key does not exist
    a_dictionary[key] = value
    return a_dictionary
