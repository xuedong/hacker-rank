#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
    
def sherlockAndAnagrams(s):
    length = len(s)
    if length <= 1:
        return 0
    
    my_dict = {}
    for l in range(1, length):
        for i in range(length-l+1):
            current = s[i:i+l]
            exist = False
            for k in my_dict.keys():
                if is_anagram(k, current):
                    my_dict[k].append([i, i+l])
                    exist = True
            if not exist:
                my_dict[current] = [[i, i+l]]
    
    count = 0
    for k in my_dict:
        current_length = len(my_dict[k])
        if current_length > 1:
            count += current_length * (current_length - 1) / 2
            
    return int(count)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()

