#!/usr/bin/python3
"""
This module defines a function to check if
an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to test.
        a_class: The class to check against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
