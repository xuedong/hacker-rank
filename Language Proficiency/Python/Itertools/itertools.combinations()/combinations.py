#!/bin/python3
from itertools import combinations

if __name__ == "__main__":
    string, n = input().split()
    n = int(n)

    for i in range(n):
        print("\n".join(map("".join, list(combinations(sorted(string), i+1)))))

