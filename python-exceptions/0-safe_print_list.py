#!/usr/bin/python3
"""
Prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    count = 0
    for i in range(x):
        try:
            # Try printing current index
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            # Stop if index goes out of range
            break
    print("")
    return count
