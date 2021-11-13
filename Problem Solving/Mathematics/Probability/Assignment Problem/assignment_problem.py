#!/usr/bin/env python3
from decimal import Decimal


def partial(M, N, k):
    if k == 0:
        return 0

    s = Decimal(1)
    q = Decimal(1)
    for i in range(min(M//k, N)):
        q *= Decimal(-(N-i)) / Decimal(i+1)
        for j in range(k):
            q *= Decimal((M-i*k-j)) / Decimal((N+M-i*k-1-j))
        s += q
    return float(s)


def solve(M, N):
    before = 0
    res = 0
    for k in range(1, M+1):
        after = partial(M, N, k+1)
        res += k * (after - before)
        before = after
    return res


if __name__ == "__main__":
    cases = int(input())

    for _ in range(cases):
        M, N = map(int, input().split())
        res = solve(M, N)

        print(res)

