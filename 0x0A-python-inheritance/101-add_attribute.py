#!/usr/bin/python3
''' init '''


def add_attribute(obj, name, value):
    '''
    Adds attribute
    '''
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
