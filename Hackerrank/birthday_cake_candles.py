#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    largest = 0
    for i in ar:
        if i > largest:
            largest = i
        else:
            continue
    
    result = ar.count(largest)
    return result
    
    

if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    
