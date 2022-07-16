#!/usr/bin/env python3

import math


def pearson(x, y, n):
    mx, my = sum(x)/n, sum(y)/n

    numerator = sum([(x[i]-mx)*(y[i]-my) for i in range(n)])
    sigma_x = math.sqrt(sum([(x[i]-mx)**2 for i in range(n)]))
    sigma_y = math.sqrt(sum([(y[i]-my)**2 for i in range(n)]))

    rho = numerator / (sigma_x * sigma_y)
    return rho

if __name__ == "__main__":
    n = int(input())
    m, p, c = [], [], []
    for _ in range(n):
        mi, pi, ci = list(map(int, input().split()))
        m.append(mi)
        p.append(pi)
        c.append(ci)

    print(round(pearson(m, p, n), 2))
    print(round(pearson(p, c, n), 2))
    print(round(pearson(c, m, n), 2))

