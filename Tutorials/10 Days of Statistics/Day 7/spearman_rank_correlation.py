#!/bin/python3

def get_rank(arr):
    n = len(arr)
    rank = [0 for i in range(n)]

    for i in range(n):
        rank_i = 0
        for j in range(n):
            if arr[j] > arr[i]:
                rank_i += 1
        rank[i] = rank_i + 1

    return rank

def spearman(rank1, rank2, n):
    total = 0
    for i in range(n):
        total += (rank1[i] - rank2[i]) ** 2
    
    return 1 - 6*total/(n*(n**2-1))

n = int(input())
arr1 = [float(arr_i) for arr_i in input().strip().split(' ')]
arr2 = [float(arr_i) for arr_i in input().strip().split(' ')]

print(round(spearman(get_rank(arr1), get_rank(arr2), n), 3))

