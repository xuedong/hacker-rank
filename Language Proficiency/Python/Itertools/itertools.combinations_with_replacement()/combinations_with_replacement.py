#!/usr/bin/env python3
from itertools import combinations_with_replacement


if __name__ == "__main__":
    string, n = input().split()

    print('\n'.join(map(''.join, list(combinations_with_replacement(sorted(string), int(n))))))

