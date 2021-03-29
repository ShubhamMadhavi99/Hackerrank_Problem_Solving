#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    s = 0
    t = 0
    n = len(a)

    for i in range(0,n,1):
        if a[i] == b[i]:
            s = s + 0
        elif a[i] > b[i]:
            s = s + 1
        elif a[i] < b[i]:
            t = t + 1
    return (s,t)
    
    

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

