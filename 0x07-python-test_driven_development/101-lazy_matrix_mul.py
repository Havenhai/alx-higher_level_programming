#!/usr/bin/python3
# 101-lazy_matrix_mul.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication matrices.

    Args:
        m_a : The first matrix.
        m_b : The second matrix.
    """

    return (np.matmul(m_a, m_b))
