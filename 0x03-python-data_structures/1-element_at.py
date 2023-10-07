#!/usr/bin/python3
# 1-element_at.py


def element_at(my_havulist, idx_havu):
    """Retrive an element from a list."""
    """Check if the(negative or greater than the last valid index)"""
    if idx_havu < 0 or idx_havu > (len(my_havulist) - 1):
        return None
    """Retrieve and return the element at the specified index."""
    return (my_havulist[idx_havu])
