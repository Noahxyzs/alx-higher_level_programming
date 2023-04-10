#!/usr/bin/python3
'''
    MyInt
'''


class MyInt(int):
    ''' class '''
    def __eq__(self, val):
        ''' eq '''
        return self.number != val

    def __str__(self):
        ''' str '''
        return str(self.number)

    def __init__(self, number):
        ''' init '''
        self.number = number

    def __ne__(self, val):
        ''' ne '''
        return self.number == val
