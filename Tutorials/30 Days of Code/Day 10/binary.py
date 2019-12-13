#!/bin/python3

import sys
import re

n = int(input().strip())
binary = "{0:b}".format(n)

max_len = max([len(s) for s in re.findall(r'1+', binary)])

print(max_len)
