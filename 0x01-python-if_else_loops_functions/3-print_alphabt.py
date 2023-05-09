#!/usr/bin/python3
num = " "
for i in range(97, 123):
    if i == 101 or 1 == 113:
        continue
    num = chr(i)
    print("{}" .format(num), end="")
