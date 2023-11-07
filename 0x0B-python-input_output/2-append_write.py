#!/usr/bin/python3
"""Writes file-appending function."""


def append_write(filename="", text=""):
    """Appends string to the end UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
