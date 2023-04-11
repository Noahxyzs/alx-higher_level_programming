#!/usr/bin/python3
"""student"""


class Student:
    """class name Student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic

    def reload_from_json(self, json):
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
