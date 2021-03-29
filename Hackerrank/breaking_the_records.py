#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h = 0
    l = 0
    highest = scores[0]
    lowest = scores[0]

    for i in scores:
        if i > highest:
            highest = i
            h = h + 1
            
        elif i < lowest:
            lowest  = i
            l = l + 1
        
    print(h,l)
    return (h,l)


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

