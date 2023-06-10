#!/usr/bin/python3
""" prints a text with 2 new lines """


def text_indentation(text):
    """ prints a text with 2 new lines """

    chars = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in text:
            print(i, end='')
            if i in chars:
                print('\n\n', end='')
