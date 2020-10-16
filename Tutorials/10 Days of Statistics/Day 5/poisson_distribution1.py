#!/bin/python3
import sys
from math import factorial as fac
from math import exp


def poisson_dist(lam, k):
    return lam**k * exp(-lam) / fac(k)

lam = float(input())
k = int(input())

print(round(poisson_dist(lam, k), 3))

