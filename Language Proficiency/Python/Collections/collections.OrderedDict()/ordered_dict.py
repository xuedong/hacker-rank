#!/usr/bin/env python3

from collections import OrderedDict


if __name__ == "__main__":
    N = int(input())
    items = OrderedDict()

    for i in range(N):
        entry = input().rpartition(' ')
        item, price = entry[0], int(entry[2])
        if item in items:
            items[item] += price
        else:
            items[item] = price

    for item in items:
        print(item, items[item])

