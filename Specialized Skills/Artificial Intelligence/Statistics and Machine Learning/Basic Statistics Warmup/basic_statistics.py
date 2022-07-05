#!/usr/bin/env python3

import math
from typing import List, Tuple
from collections import Counter


class Statistics(object):
    def __init__(self, arr: List):
        self.arr = arr
        self.length = len(self.arr)
        self.sorted_arr = sorted(self.arr)
        self.counts = Counter(arr)

    def mean(self) -> float:
        return sum(self.arr) / self.length

    def median(self) -> float:
        if self.length % 2 == 1:
            return self.sorted_arr[self.length//2]
        else:
            return (self.sorted_arr[self.length//2-1] + self.sorted_arr[self.length//2]) / 2

    def mode(self) -> int:
        modes = [key for key, value in self.counts.items() if value == self.counts.most_common(1)[0][1]]
        return min(modes)

    def std(self) -> float:
        mean = self.mean()
        sd = 0
        for num in self.arr:
            sd += (num - mean) ** 2
        return math.sqrt(sd/self.length)

    def ci95(self) -> Tuple[float, float]:
        sd = self.std()
        bonus = 1.96*sd/math.sqrt(self.length)
        return self.mean()-bonus, self.mean()+bonus


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    stats = Statistics(arr)
    print(stats.mean())
    print(stats.median())
    print(stats.mode())
    print(round(stats.std(), 1))
    print(round(stats.ci95()[0], 1), round(stats.ci95()[1], 1))

