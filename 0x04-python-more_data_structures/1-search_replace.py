#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    value = 0
    for i in my_list:
        if i is search:
            new_list[value] = replace
        value += 1
    return (new_list)
