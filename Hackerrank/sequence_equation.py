#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    for i in range(0,len(p)):
        x = p[i]
        print(x)

if __name__ == '__main__':


    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

