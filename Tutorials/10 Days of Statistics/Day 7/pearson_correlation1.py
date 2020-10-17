#!/bin/python3
from math import sqrt


def mean(arr, n):
    return sum(arr)/n

def std(arr, mean, n):
    s = 0
    for i in range(n):
        s += (arr[i]-mean)**2
    return sqrt(s/n)

def pearson(arr1, arr2, n):
    mu1 = mean(arr1, n)
    mu2 = mean(arr2, n)
    std1 = std(arr1, mu1, n)
    std2 = std(arr2, mu2, n)
    
    cov = 0
    for i in range(n):
        cov += (arr1[i] - mu1) * (arr2[i] - mu2)
    cov /= n
    pearson = cov / (std1 * std2)
    return pearson

n = int(input())
arr1 = [float(arr_i) for arr_i in input().strip().split(' ')]
arr2 = [float(arr_i) for arr_i in input().strip().split(' ')]

print(pearson(arr1, arr2, n))

