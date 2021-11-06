#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def print_crossword(crossword):
    for row in crossword:
        print(''.join(row))

def possible_positions(crossword, word):
    positions = []
    n = len(word)

    for i in range(10):
        for j in range(11-n):
            flag = True
            for k in range(n):
                if crossword[i][j+k] not in ['-', word[k]]:
                    flag = False
                    break
            if flag:
                positions.append((i, j, 0))

    for i in range(11-n):
        for j in range(10):
            flag = True
            for k in range(n):
                if crossword[i+k][j] not in ['-', word[k]]:
                    flag = False
                    break
            if flag:
                positions.append((i, j , 1))

    return positions

def remove(crossword, word, position):
    i, j, axis = position
    n = len(word)
    if axis == 0:
        for k in range(n):
            crossword[i][j+k] = '-'
    else:
        for k in range(n):
            crossword[i+k][j] = '-'

def write(crossword, word, position):
    i, j , axis = position
    n = len(word)
    if axis == 0:
        for k in range(n):
            crossword[i][j+k] = word[k]
    else:
        for k in range(n):
            crossword[i+k][j] = word[k]

def crosswordPuzzle(crossword, words):
    global solved
    num_words = len(words)
    if num_words == 0:
        if not solved:
            print_crossword(crossword)
        solved = True
        return

    word = words.pop()
    positions = possible_positions(crossword, word)

    for position in positions:
        write(crossword, word, position)
        crosswordPuzzle(crossword, words)
        remove(crossword, word, position)

    words.append(word)


if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        crossword.append(list(input()))
    words = str(input()).split(";")

    solved = False
    crosswordPuzzle(crossword, words)

