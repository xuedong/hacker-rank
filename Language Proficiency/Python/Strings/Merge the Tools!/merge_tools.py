#!/usr/bin/env python3


def merge_the_tools(string, k):
    # your code goes here
    temp = []
    length = 0
    for char in string:
        if char not in temp:
            temp.append(char)
        length += 1
        if length == k:
            print(''.join([char for char in temp]))
            temp = []
            length = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

