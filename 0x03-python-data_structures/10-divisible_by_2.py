#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        pass
    else:
        evens = []
        for i in range(len(my_list) - 1):
            if i % 2 == 0:
                evens.append(True)
            else:
                evens.append(False)
        return evens
