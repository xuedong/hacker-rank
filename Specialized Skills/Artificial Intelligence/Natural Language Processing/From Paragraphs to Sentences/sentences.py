#!/usr/bin/env python3


if __name__ == "__main__":
    text = input().strip()
    start = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            if text[i+1] == '"' or text[i+1] == ":":
                continue

            print(text[start:i+1])
            start = i+1

