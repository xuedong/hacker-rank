#!/bin/python3

if __name__ == "__main__":
    set_a = set(input().split())
    n = int(input())
    print(all(set_a > set(input().split()) for _ in range(n)))

