#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    s = 0
    for i in ar:
        s = s + i
    return s


if __name__ == '__main__':
    

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    
