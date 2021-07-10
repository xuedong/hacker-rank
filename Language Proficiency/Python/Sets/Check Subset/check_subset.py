#!/bin/python3

if __name__ == "__main__":
    testCases = int(input())
    for _ in range(testCases):
        m = int(input())
        set_a = set(input().split())
        n = int(input())
        set_b = set(input().split())

        print(set_a.issubset(set_b))

