#!/bin/python3
from math import sqrt


samples = float(input())
mu = float(input())
std = float(input())
confidence = float(input())
zscore = float(input())

lower = samples * mu - zscore * sqrt(samples) * std
upper = samples * mu + zscore * sqrt(samples) * std

print(round(lower/100, 2))
print(round(upper/100, 2))

