#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    y = 5
    tot = 0
    for _ in range(0,n,1):
        #print(y)
        x = math.floor(y/2)
        #print(x)
        tot = tot + x
        y = x * 3
        #print(y)
    print(tot)
    return (tot)



if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

