#!/usr/bin/env python3

import math


def std(arr: list) -> float:
    mean = sum(arr) / len(arr)
    var = sum([(element-mean)**2 for element in arr]) / len(arr)
    return math.sqrt(var)


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    # print(std(arr1))
    # 9n^2 - 36n + 28 = 0
    delta = 36 ** 2 - 4 * 9 * 28
    print(round((36 + math.sqrt(delta)) / 18, 2))

