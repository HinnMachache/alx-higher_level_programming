#!/usr/bin/python3
# 2-is_same_class.py
"""s_same_class: Returns True if object is
an exact instance of the specified class
Arguments:
    obj: Object created
    a_class: Class
"""


def is_same_class(obj, a_class):
    """Functions that returns true if
    object is an exact instance of the
    specified class"""
    return (type(obj) is a_class)
