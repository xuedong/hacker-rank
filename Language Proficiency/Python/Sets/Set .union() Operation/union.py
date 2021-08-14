#!/usr/bin/env python3


if __name__ == '__main__':
    n = int(input())
    subs_a = set(map(int, input().split()))
    m = int(input())
    subs_b = set(map(int, input().split()))

    print(len(subs_a|subs_b))

