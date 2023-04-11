#!/usr/bin/python3
"""save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """wright .txt"""
    with open(filename, 'w') as f:
        file_json = json.dumps(my_obj)
        f.write(file_json)
    f.close()
