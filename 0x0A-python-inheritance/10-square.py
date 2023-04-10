#!/usr/bin/python3
'''
    rectangle class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        square
    '''
    def __init__(self, size):
        ''' init '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' area '''
        return self.__size ** 2
