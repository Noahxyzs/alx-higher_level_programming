#!/usr/bin/python3
''' inherits '''


def inherits_from(obj, a_class):
    '''function returns true'''
    return isinstance(obj, a_class) and type(obj) is not a_class
