#!/bin/python3
import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())

    print(str(round(math.degrees(math.atan2(AB, BC))))+u'\N{DEGREE SIGN}')

