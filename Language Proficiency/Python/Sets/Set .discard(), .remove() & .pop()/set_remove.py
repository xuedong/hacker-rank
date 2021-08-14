#!/usr/bin/env python3


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        eval("s.{0}({1})".format(*input().split()+['']))

    print(sum(s))

