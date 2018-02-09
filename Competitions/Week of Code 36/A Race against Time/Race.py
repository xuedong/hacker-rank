#!/bin/python3

import sys

def raceAgainstTime(n, mason_height, heights, prices):
    dp = [[0 for dummy_i in range(n)] for dummy_j in range(n)]
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(i, n):
            if j == n-1:
                carrier_height = mason_height
            else:
                carrier_height = heights[n-2-j]
            position_height = heights[n-1-i]
            if carrier_height < position_height:
                time = 1 + position_height - carrier_height
                price = prices[n-1-i]
                idx = heights.index(position_height)
                if idx == n-1:
                    dp[i][j] = time + price + dp[i-1][n-1]
                else:
                    dp[i][j] = time + price + dp[i-1][n-2-idx]
            elif carrier_height == position_height and prices[0] < 0:
                time = 1
                price = prices[n-1-i]
                dp[i][j] = time + price + dp[i-1][j-1]
            elif prices[0] >= 0:
                time = 1
                price = 0
                dp[i][j] = time + price + dp[i-1][j]
            else:
                time1 = 1 + carrier_height - position_height
                price1 = prices[n-1-i]
                idx = heights.index(position_height)
                time2 = 1
                price2 = 0
                if idx == n-1:
                    total1 = time1 + price1 + dp[i-1][n-1]
                else:
                    total1 = time1 + price1 + dp[i-1][n-2-idx]
                total2 = time2 + price2 + dp[i-1][j]
                dp[i][j] = min(total1, total2)
    #print(dp)
    return dp[n-1][n-1]

def raceAgainstTime_bis(n, mason_height, heights, prices):
    # Complete this function
    def aux(carrier_height, heights, prices):
        if len(heights) == 0:
            return 1
        elif carrier_height < heights[0]:
            time = 1 + heights[0] - carrier_height
            price = prices[0]
            carrier_height = heights[0]
            rest = aux(carrier_height, heights[1:], prices[1:])
            total = time + price + rest
            return total
        elif prices[0] >= 0:
            time = 1
            price = 0
            rest = aux(carrier_height, heights[1:], prices[1:])
            total = time + price + rest
            return total
        else:
            time1 = 1 + carrier_height - heights[0]
            price1 = prices[0]
            carrier_height1 = heights[0]
            time2 = 1
            price2 = 0
            carrier_height2 = carrier_height
            total1 = time1 + price1 + aux(carrier_height1, heights[1:], prices[1:])
            total2 = time2 + price2 + aux(carrier_height2, heights[1:], prices[1:])
            return min(total1, total2)
    return aux(mason_height, heights, prices)


if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)

