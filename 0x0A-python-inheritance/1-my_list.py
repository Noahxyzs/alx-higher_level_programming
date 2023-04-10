#!/usr/bin/python3
'''
    Inherits attributes from calss list
'''


class MyList(list):
    '''
        it prints list in ascending order
    '''
    def print_sorted(self):
        print(sorted(self))
