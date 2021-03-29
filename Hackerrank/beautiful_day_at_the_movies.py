#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k): 
    lst = []
    rev = []
    
    for l in range(i,j+1,1):
        x = str(l)
        lst.append(x)
        rev.append(x[::-1])
    
    # print(rev)
    # print(lst)
    count = 0
    l = len(lst)
    for i in range(0,l,1):
        d = ((int(lst[i]) - int(rev[i]))) / k
        if (d - int(d)) == 0:
            count = count + 1
        else:
            continue
    # print(count)
    return count
        


if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)
    

