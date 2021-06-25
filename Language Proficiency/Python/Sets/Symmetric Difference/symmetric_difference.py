#!/bin/python3

if __name__ == '__main__':
    M = int(input())
    a = set(input().split())
    N = int(input())
    b = set(input().split())

    print('\n'.join(sorted(a.difference(b).union(b.difference(a)), key=int)))

