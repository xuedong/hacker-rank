#!/usr/bin/env python2


if __name__ == "__main__":
    # E[X^2] = Var(X) + E[X]^2 = lambda^2 + lambda
    c_a = 160 + 40 * (0.88 ** 2 + 0.88)
    c_b = 128 + 40 * (1.55 ** 2 + 1.55)
    print round(c_a, 3)
    print round(c_b, 3)

