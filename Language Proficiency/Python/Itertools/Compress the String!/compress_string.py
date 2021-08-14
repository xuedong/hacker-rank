#!/usr/bin/env python3

from itertools import groupby


if __name__ == "__main__":
    string = input()

    print(*[(len(list(it)), int(key)) for key, it in groupby(string)])

