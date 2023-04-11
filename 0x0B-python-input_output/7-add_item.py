#!/usr/bin/python3
import json
from sys import argv
"""
function that add and save
"""


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new = load_json(filename)
except (ValueError, FileNotFoundError):
    new = []

new = new + argv[1:]
save_json(new, filename)
