#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = 0
    
    for i in a:
        if i <= 1:
            count = count + 1
        else:
            continue
    print(count)
    if count < k:
        print("YES")
        return ("YES")
    else:
        print("NO")
        return ("NO")

if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
