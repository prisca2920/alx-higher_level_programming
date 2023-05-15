#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if i < 0 or i >= len(my_list):
            return my_list
        else:
            del my_list[idx]
            return my_list
