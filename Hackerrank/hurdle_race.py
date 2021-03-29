#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    largest  = 0
    for i in height:
        if i > largest:
            largest = i
    x = largest - k
    if x<0:
        return "0"
    else:
        return x

if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)
    print(result)

