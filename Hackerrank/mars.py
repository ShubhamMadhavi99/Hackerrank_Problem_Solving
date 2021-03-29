#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    # n = 3
    # count = 0

    # for i in range(0,len(s),n):
    #     three = (s[i:i+n])
    #     print(three)
    #     if three != "SOS":
    #         count = count + 1
        
    # return count
    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)
    print(result)

