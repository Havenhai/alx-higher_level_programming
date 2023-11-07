#!/usr/bin/python3
"""Write a function that reads and prints it to stdout."""


def read_file(filename=""):
    """Print the contents UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
