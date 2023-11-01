#!/usr/bin/python3
# 5-text_indentation.py
"""Defines tation function."""


def text_indentation(text):
    """Print with two new lines after each '.', '?', and ':'.

    Args:
        text (string): txt to print.
    Raises:
        TypeError: txt is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
