#!/usr/bin/env python3


if __name__ == "__main__":
    # P(500-y < X < 500+y) = 0.95 where X ~ N(500, 8)
    # That's 2 std
    y = 1.96 * 8
    print(round(500-y, 2))
    print(round(500+y, 2))

