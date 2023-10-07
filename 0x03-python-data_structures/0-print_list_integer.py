#!/usr/bin/python3

def print_integers(input_list=None):
    """Print all integers in the given list."""
    if input_list is None:
        input_list = []

    for element in input_list:
        if isinstance(element, int):
            print(element)
