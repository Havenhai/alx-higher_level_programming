#!/usr/bin/python3
# 4-print_square.py
"""Defines printing function."""


def print_square(size):
    """Print square the # character.

    Args:
        size (int): height/width of square.
    Raises:
        TypeError: size an integer.
        ValueError: size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
