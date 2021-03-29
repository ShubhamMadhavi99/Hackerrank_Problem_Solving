#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = 0
    l = []
    largest = 0
    
    for i in arr:
        s = s + i
    
    for j in arr:
        t = s - j
        l.append(t)
    
    smallest = l[0]
    for x in l:
        if x > largest:
            largest = x
        else:
            continue

    for x in l:
        if smallest > x:
            smallest = x
        else:
            continue

    print(largest)
    print(smallest)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
