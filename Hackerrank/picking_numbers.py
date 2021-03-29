#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
n=int(input())
l=[int(i) for i in input().split()]
maximum=0
for i in l:
    c=l.count(i)
    print(" ")
    print(c)
    d=l.count(i-1)
    print(" ")
    print(d)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)
