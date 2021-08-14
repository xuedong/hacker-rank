#!/usr/bin/env python3

from itertools import combinations


if __name__ == "__main__":
    N = int(input())
    string = ''.join(input().split())
    K = int(input())

    l = list(combinations(string, K))
    l_a = [e for e in l if 'a' in e]
    total = len(l)
    total_a = len(l_a)
    print(total_a/total)

