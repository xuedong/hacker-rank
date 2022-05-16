#!/usr/bin/env python2

import math


if __name__ == "__main__":
    # Find P(k = 5) = lambda^k * e^-lambda / k!
    prob = 2.5 ** 5 * math.exp(-2.5) / 120
    print round(prob, 3)

