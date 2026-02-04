#!/usr/bin/python3
"""
    Function file for lookup.
"""


def lookup(obj):
    """
        Returns the list of available attributes
        and methods of an object.
        Args:
            obj (class): The object to inspect.
    """
    return dir(obj)
