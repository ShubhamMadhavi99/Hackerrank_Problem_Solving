#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#

def simpleArraySum(ar):
    s = 0
    for i in ar:
        s = s + i
        
    return s

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = simpleArraySum(ar)
