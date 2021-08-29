#!/usr/bin/env python3

from collections import OrderedDict


if __name__ == "__main__":
    n = int(input())
    d = OrderedDict()

    total = 0
    for _ in range(n):
        word = input()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
            total += 1

    print(total)
    print(*(d.values()))

