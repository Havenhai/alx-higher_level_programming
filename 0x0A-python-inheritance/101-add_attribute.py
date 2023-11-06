#!/usr/bin/python3
# 101-add_attribute.py
"""Defines function that adds attributes objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to object if possible.

    Args:
        obj (any): The object to]] add an attribute to.
        att (str): The name of the]] attribute to add to obj.
        value (any): The value]] of att.
    Raises:
        TypeError: If the attribute ]]cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
