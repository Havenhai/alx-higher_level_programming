#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_haven_list, idx_haven, element_haven):
    """Replace an element of a list at a specific position."""
    if idx_haven >= 0 and idx_haven < len(my_haven_list):
        my_haven_list[idx_haven] = element_haven
    return (my_haven_list)

