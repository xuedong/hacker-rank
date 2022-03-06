#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    prefix_set = set()
    word_set = set()

    for word in words:
        if word in prefix_set:
            print("BAD SET")
            print(word)
            return

        prefix = ''
        for char in word:
            prefix += char
            prefix_set.add(prefix)
            if prefix in word_set:
                print("BAD SET")
                print(word)
                return
        word_set.add(word)

    print("GOOD SET")


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

