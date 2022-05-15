#!/usr/bin/env python3


if __name__ == "__main__":
    mean = 0.675
    std = 0.065
    z_score = (0.9025 - mean) / 0.065
    print(round(z_score, 2))

