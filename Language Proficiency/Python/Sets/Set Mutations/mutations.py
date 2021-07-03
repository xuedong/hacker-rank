#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        cmd, _ = input().split()
        set2 = set(map(int, input().split()))
        eval("set1.{0}({1})".format(cmd, set2))

    print(sum(set1))

