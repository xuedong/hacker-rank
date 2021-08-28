#!/usr/bin/env python3

from collections import deque


if __name__ == "__main__":
    N = int(input())
    d = deque()
    for _ in range(N):
        eval("d.{0}({1})".format(*input().split()+['']))

    print(*d)

