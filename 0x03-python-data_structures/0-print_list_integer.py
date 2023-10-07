#!/usr/bin/python3
# 0-print_list_integer.py

def print_havu_list_integer(havu_list=[]):
    """Print all integers in the provided list.
    Args:
        int_list (list[int]): The list containing integers to be printed."""
    for i_haven in range(len(havu_list)):
        print("{:d}".format(havu_list[i_haven]))
