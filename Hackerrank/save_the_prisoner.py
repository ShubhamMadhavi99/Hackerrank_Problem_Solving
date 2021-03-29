#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
#n,the number of prisoners
# m : the number of sweets
# s : the chair number to start passing out treats at

def saveThePrisoner(n, m, s):
    save = 0
    
    if s == n:
        for i in range (1,m,1):
            save = i + s
    else:
        continue

    print(save)
if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

