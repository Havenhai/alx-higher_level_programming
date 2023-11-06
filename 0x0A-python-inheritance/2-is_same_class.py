#!/usr/bin/python3
# 2-is_same_class.py
# HAVEN
"""Defines class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is exactly instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
