#!/usr/bin/python3
"""creates an Object from a json file"""
import json


def load_from_json_file(filename):
    """creates an obj from json"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
