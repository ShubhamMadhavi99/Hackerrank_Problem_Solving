#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy as np

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
#def diagonalDifference(arr)
    # arr2 = np.array(arr)
    # x = arr2[0,0] + arr2 [1,1] + arr2[2,2]
    # y = arr2[0,2] + arr2 [1,1] + arr2[2,0]
    # z = x - y
    # z = abs(z)
    # return z
    

    left,right,i=0,0,0
    while i != n:
        left+=arr[i][i]
        right+=arr[i][n-1-i]
        i+=1
    return abs(left-right)
        


if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)
# result = diagonalDifference(arr)

    
