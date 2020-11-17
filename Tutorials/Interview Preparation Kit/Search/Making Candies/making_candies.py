#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(machines, workers, price, candies):
    current_machines = machines
    current_workers = workers
    current_candies = 0
    current_passes = 0
    final_passes = sys.maxsize
    while current_candies < candies:
        passes = (price - current_candies) // (current_machines * current_workers)
        if passes <= 0:
            increase_units = current_candies // price
            current_candies %= price
            total_units = current_machines + current_workers + increase_units
            half_units = math.ceil(total_units/2)
            if current_machines >= current_workers:
                current_machines = max(half_units, current_machines)
                current_workers = total_units - current_machines
            else:
                current_workers = max(half_units, current_workers)
                current_machines = total_units - current_workers
            passes = 1
        current_candies += passes * current_machines * current_workers
        current_passes += passes
        final_passes = min(final_passes, current_passes + math.ceil((candies - current_candies) / (current_machines * current_workers)))
    return min(final_passes, current_passes)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()

