#!/bin/python3
import sys
from math import erf, sqrt


def phi(x, mu, std):
    return (1.0 + erf((x-mu) / (std*sqrt(2.0)))) / 2.0

total = float(input())
number = float(input())
mu = float(input())
std = float(input())

print(round(phi(total, number*mu, sqrt(number)*std), 4))

