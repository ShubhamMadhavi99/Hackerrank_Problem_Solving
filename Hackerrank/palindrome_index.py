#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    lst = []
    x = ""
    for i in s:
        x = i + x
    
    if x == s:
        print ("-1")
        return ("-1")
    else:
        for i in x:
            lst.append(i)
        
        for j in lst:
            lst.remove(j)
            k = "".join(lst)
            x = ""
            for i in s:
                x = i + x
                
            
            if x == k:
                lst.append(j)
            else:
                print(j)

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

