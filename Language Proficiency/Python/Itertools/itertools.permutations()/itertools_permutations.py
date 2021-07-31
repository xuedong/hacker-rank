#!/bin/python3
from itertools import permutations


if __name__ == "__main__":
    S, n = input().split()
    n = int(n)

    print('\n'.join(map(''.join, sorted(list(permutations(S, n))))))

