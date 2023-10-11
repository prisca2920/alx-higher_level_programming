#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key, value in a_dictionary.items():
        a_dictionary[key] = value
        return a_dictionary
    
