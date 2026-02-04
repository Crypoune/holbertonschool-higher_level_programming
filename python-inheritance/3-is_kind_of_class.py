#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of,
or if it inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or inherits from, the specified class.

    Args:
        obj: The object to test.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class
        or its subclasses, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
