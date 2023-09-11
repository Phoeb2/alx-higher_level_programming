#!/usr/bin/python3
"""
lookup - It returns the list of available attributes and methods of an object
@obj: the object
Return: list of object
"""


def lookup(obj):
    """ return list of obj """
    return dir(obj)
