#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """function that appends a string in .txt file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    f.close()
    return len(text)
