#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list only once for each integer."""
    # Convert list to a set to remove duplicates, then calculate the sum
    return sum(set(my_list))
