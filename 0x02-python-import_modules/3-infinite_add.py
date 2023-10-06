#!/usr/bin/python3
import sys

if __name__ == '__main__':
    counter = 0

    for i in range(len(sys.argv) - 1):
        counter += int(sys.argv[i + 1])
    print('{}'.format(counter))
