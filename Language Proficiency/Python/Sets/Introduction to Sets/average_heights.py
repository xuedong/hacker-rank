#!/usr/bin/env python3


def average(array):
    # your code goes here
    heights = set(array)
    return sum(heights)/len(heights)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

