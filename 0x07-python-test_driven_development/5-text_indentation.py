#!/usr/bin/python3
"""prints a text with 2 new lines after . ? or :"""


def text_indentation(text):
    """prints a text with 2 new lines after . ? or :"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    count = 0
    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        print(text[count], end="")

        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count += 1
