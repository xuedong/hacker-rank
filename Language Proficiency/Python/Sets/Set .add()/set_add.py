#!/usr/bin/env python3


if __name__ == '__main__':
    stamps = set()

    num = int(input())
    for _ in range(num):
        stamp = input()
        stamps.add(stamp)

    print(len(stamps))

