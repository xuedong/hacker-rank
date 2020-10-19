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

def linear_regression(arr_x, arr_y, n):
    mu_x = mean(arr_x, n)
    mu_y = mean(arr_y, n)
    std_x = std(arr_x, mu_x, n)
    std_y = std(arr_y, mu_y, n)
    rho = pearson(arr_x, arr_y, n)

    b = rho * std_y / std_x
    a = mu_y - b * mu_x
    return a, b

arr_x = [95, 85, 80, 70, 60]
arr_y = [85, 95, 70, 65, 70]
n = 5
a, b = linear_regression(arr_x, arr_y, n)
y = a + b * 80
print(round(y, 3))

