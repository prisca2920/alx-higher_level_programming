#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        while(x):
            for i in my_list:
                print(i)
                x += 1
                return x
    except Exception as e:
        print(e)
