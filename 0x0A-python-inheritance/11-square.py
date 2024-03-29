#!/usr/bin/python3
''' init '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square '''

    def __init__(self, size):
        ''' init '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        ''' str '''
        return "[Square] {}/{}".format(self.__size, self.__size)
