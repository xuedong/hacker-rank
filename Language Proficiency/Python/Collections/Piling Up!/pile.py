#!/usr/bin/env python3

from collections import deque


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        queue = deque(map(int, input().split()))

        flag = True
        for cube in reversed(sorted(queue)):
            if queue[0] == cube:
                queue.popleft()
            elif queue[-1] == cube:
                queue.pop()
            else:
                print("No")
                break
        else: print("Yes")

