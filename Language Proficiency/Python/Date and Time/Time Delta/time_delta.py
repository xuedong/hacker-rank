#!/usr/bin/env python3

from datetime import datetime


if __name__ == "__main__":
    T = int(input())
    fmt = "%a %d %b %Y %H:%M:%S %z"
    for _ in range(T):
        print(int(abs((datetime.strptime(input(), fmt) - datetime.strptime(input(), fmt)).total_seconds())))

