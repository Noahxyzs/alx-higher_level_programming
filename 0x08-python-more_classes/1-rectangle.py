#!/usr/bin/python3
"""create 1-rectangel.py"""


class Rectangle:
    """initialize"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter set in width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter set in height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter get height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
