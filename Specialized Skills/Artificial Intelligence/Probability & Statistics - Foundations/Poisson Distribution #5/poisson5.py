#!/usr/bin/env python2

import math


if __name__ == "__main__":
    # 1. Poisson(1.2), compute P(X = 2)
    p1 = 1.2 ** 2 * math.exp(-1.2) / 2
    print round(p1, 3)

    # 2. Poisson(1.2), compute P(X < 3)
    p2 = math.exp(-1.2) + 1.2 * math.exp(-1.2) + p1
    print round(p2, 3)

    # 3. Poisson(1.2*10), compute P(X = 5)
    p3 = 12 ** 5 * math.exp(-12) / 120
    print round(p3, 3)

    # 4. Poisson(1.2*40), compute P(X >= 3) = 1 - P(X = 0) - P(X = 1) - P(X = 2)
    p4 = 1 - math.exp(-48) - 48 * math.exp(-48) - 48 ** 2 * math.exp(-48) / 2
    print round(p4, 3)

