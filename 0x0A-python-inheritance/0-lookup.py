#!/usr/bin/python3
"""
Contains method lookup that returns a list of object's attribute and methods
"""


def lookup(obj):
    """returns a list of object's attribute and methods"""
    return dir(obj)
