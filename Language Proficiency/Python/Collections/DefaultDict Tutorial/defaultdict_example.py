#!/usr/bin/env python3

from collections import defaultdict


if __name__ == "__main__":
    n, m = map(int, input().split())

    d = defaultdict(list)
    l = []

    for i in range(n):
        d[input()].append(i+1)

    for _ in range(m):
        l.append(input())

    for j in range(m):
        if l[j] in d:
            print(" ".join(map(str, d[l[j]])))
        else:
            print(-1)

