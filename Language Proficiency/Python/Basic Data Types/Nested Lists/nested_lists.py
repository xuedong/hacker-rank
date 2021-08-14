#!/usr/bin/env python3


if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    second_lowest = sorted(list(set([score for _, score in scores])))[1]
    print('\n'.join([name for name, score in sorted(scores) if score == second_lowest]))

