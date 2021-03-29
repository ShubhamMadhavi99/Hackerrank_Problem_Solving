#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    lst = []
    
    for i in range(65,91,1):
        lst.append(chr(i))
    for i in range(97,123,1):
        lst.append(chr(i))
    lst.append(chr(32))
    #print(lst)
    
    for i in s:
        if i in lst:
            print("pangram")
        else:
            print("not pangram")

if __name__ == '__main__':

    s = input()

    result = pangrams(s)

