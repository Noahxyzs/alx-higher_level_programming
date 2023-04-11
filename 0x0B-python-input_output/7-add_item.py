#!/usr/bin/python3
''' add_item '''
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args="", filename=""):
    '''
    add item
    '''
    try:
        allArgs = load_from_json(filename)
    except Exception as e:
        allArgs = []

    for item in args:
        allArgs.append(item)
    save_to_json(allArgs, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
