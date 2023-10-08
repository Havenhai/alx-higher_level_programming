#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_havu_list, idx_havu, element_havu):
    """Replace element of list at a specific position."""
    """ Check if the provided index is within the list length)."""
    if idx_havu >= 0 and idx_havu < len(my_havu_list):
    """the index is valid, replace the element index with provided element."""
     my_havu_list[idx_havu] = element_havu
    """Return the modified list"""
    return (my_havu_list)
