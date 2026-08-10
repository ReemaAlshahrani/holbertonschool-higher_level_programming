#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    # Create a new list replacing search element with replace element
    return [replace if element == search else element for element in my_list]
