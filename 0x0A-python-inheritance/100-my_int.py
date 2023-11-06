#!/usr/bin/python3
# 100-my_int.p
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """Invert intigera operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
