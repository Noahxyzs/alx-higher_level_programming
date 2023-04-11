#!/usr/bin/python3
"""Write_file"""


def write_file(filename="", text=""):
    """function that writes a string to .txt file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    f.close()
    return len(text)
