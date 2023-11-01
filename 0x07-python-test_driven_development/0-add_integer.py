#!/usr/bin/python3
# 0-add_integer.py
"""Integer addition function."""


def add_integer(a, b=98):
    """Return addition of a and b.

    nts are typecasted to ints addition is performed.

        TypeError: If a or b is non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
