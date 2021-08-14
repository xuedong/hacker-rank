#!/usr/bin/env python3


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = (map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))

    print(sum([(i in like) - (i in dislike) for i in arr]))

