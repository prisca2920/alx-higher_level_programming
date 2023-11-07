#!/usr/bin/python3
""" return an obj from json"""
import json


def from_json_string(my_str):
    """ return an obj from json"""
    return json.loads(my_str)
