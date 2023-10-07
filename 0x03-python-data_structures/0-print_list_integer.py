#!/usr/bin/python3
# 0-print_list_integer.py

def print_integers(int_list=None):#
    """
    Print all integers in the provided list.

    Args:
        int_list (list[int]): The list containing integers to be printed.
    """
    if int_list is None:
        int_list = []

    for num in int_list:
        if isinstance(num, int):
            print("{:d}".format(num))
