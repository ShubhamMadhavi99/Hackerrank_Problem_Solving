#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x = len(arr)
    p = 0
    neg = 0
    z = 0

    for i in arr:
        y = int(i)
        if y == 0:
            z = z + 1
        elif y == abs(y):
            p = p + 1
        else:
            neg = neg + 1
    
    print("{:.6f}".format(p/x))
    print("{:.6f}".format(neg/x))
    print("{:.6f}".format(z/x))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
