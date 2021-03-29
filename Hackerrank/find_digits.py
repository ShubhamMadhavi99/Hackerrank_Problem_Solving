#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    lst = []
    
    x = str(n)
    for i in x:
        lst.append(i)
    print(lst)

    count = 0
    for j in lst:
        if int(j) != 0:
            d = n % int(j)
            if d == 0:
                count = count + 1
            else:
                continue
        else:
            continue
    return count
        
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)
        print(result)

