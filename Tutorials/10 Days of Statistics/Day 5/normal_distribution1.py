#!/bin/python3
import sys
from math import erf, sqrt


def phi(x, mu, std):
    return (1.0 + erf((x-mu) / (std*sqrt(2.0)))) / 2.0

arr1 = [float(arr_i) for arr_i in input().strip().split(' ')]
mu = arr1[0]
std = arr1[1]
x = float(input())
arr2 = [float(arr_i) for arr_i in input().strip().split(' ')]
y1 = arr2[0]
y2 = arr2[1]

print(round(phi(x, mu, std), 3))
print(round(phi(y2, mu, std)-phi(y1, mu, std), 3))

