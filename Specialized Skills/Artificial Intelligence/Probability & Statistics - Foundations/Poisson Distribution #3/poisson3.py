#!/usr/bin/env python2

import math


if __name__ == "__main__":
    # (a). The time between calls is an exponential distribution with parameter 3
    # P = 1 - \integral_{0, 1} p(t)dt = \integral_{1, \infty} p(t)dt
    # print(round(math.exp(-3), 3))
    print("0.050")

    # (b). The probability that at least two calls will arrive in a given two minute period is P(X = 2) = 1 - P(X = 0) - P(X = 1)
    # X ~ Poisson(lambda*t) = Poisson(3*2)
    print(round(1 - math.exp(-6) - 6*math.exp(-6), 3))

