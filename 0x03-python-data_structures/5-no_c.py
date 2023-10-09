#!/usr/bin/python3
def no_c(my_string):
    sentence = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            sentence += i
    return sentence
