#!/usr/bin/python3
"""Write a mudule that permit insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing given string in file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
