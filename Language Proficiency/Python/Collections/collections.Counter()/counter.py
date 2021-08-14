#!/usr/bin/env python3

from collections import Counter


if __name__ == "__main__":
    num_shoes = int(input())
    shoes = Counter(map(int, input().split()))
    num_customers = int(input())
    res = 0

    for i in range(num_customers):
        size, price = map(int, input().split())
        if shoes[size]:
            res += price
            shoes[size] -= 1

    print(res)
