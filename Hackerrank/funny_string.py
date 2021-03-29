#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    lst = []
    for i in s:
        lst.append(ord(i))
    
    print(lst)
    
    r = []
    r = lst[::-1]
    print(r)

    l = len(lst)
    c1 = []
    c2 = []

    for n in range(1,l,1):
        d = abs(lst[n] - lst[n-1])
        e = abs(r[n] - r[n-1])
        c1.append(d)
        c2.append(e)
    print(c1)
    print(c2)

    if c1 == c2:
        return ("Funny")
        print("Funny")
    else:
        print("Not Funny")
        retrun ("NOt Funny")
    
   

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)


