#!/bin/python3
import numpy as np

m, n = [int(arr_i) for arr_i in input().strip().split(' ')]
X = np.ones((n, m+1))
y = np.zeros(n)
for i in range(n):
    arr = [float(arr_i) for arr_i in input().strip().split(' ')]
    for j in range(m):
        X[i][j+1] = arr[j]
    y[i] = arr[m]

print(X)
S = np.dot(X.T, X)
S_inv = np.linalg.inv(S)
b = np.dot(np.dot(S_inv, X.T), y.T)

q = int(input())
for i in range(q):
    x = np.ones(m+1)
    arr = [float(arr_i) for arr_i in input().strip().split(' ')]
    for j in range(1, m+1):
        x[j] = arr[j-1]
    y_out = np.dot(x, b)
    print(round(y_out, 2))

