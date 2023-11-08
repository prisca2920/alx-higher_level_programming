#!/usr/bin/python3
""" adds all args to python lst and saves"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        files = load_from_json_file("add_item.json")
    except FileNotFoundError:
        files = []
    files.extend(sys.argv[1:])
    save_to_json_file(files, "add_item.json")
