#!/usr/bin/env python3


if __name__ == '__main__':
    K = int(input())
    arr = map(int, input().split())

    s1 = set()
    s2 = set()
    for e in arr:
        if e in s1:
            s2.add(e)
        else:
            s1.add(e)

    print(s1.difference(s2).pop())

