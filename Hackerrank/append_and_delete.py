#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    lst = []
    lst2 = []
    count = 0
    for i in s:
        lst.append(i)
    
    for j in t:
        lst2.append(j)

    print(lst)
    print(lst2)

    
    
        

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)
