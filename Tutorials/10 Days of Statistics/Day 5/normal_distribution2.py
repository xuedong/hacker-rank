#!/bin/python3
import sys
from math import erf, sqrt


def phi(x, mu, std):
    return (1.0 + erf((x-mu) / (std*sqrt(2.0)))) / 2.0

arr = [float(arr_i) for arr_i in input().strip().split(' ')]
mu = arr[0]
std = arr[1]
high = float(input())
low = float(input())

print(round(100*(1-phi(high, mu, std)), 2))
print(round(100*(1-phi(low, mu, std)), 2))
print(round(100*phi(low, mu, std), 2))

