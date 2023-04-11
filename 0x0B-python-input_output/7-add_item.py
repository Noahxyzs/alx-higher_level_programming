#!/usr/bin/python3
from sys import argv
"""access"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""create"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""writes"""

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except: Exception as e
    content = []

for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, filename)
