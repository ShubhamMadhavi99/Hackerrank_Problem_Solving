#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    x = len(c)
    print(x)
    for i in range(0,x,1):
        if c[i] == '1':
            continue
        elif c[i] == '0':
            count = count + 1
            print(count)
    print(count)

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

