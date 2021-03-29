#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    t = 1
    for i in s:
        x = i.isupper()
        if x == True:
            t = t + 1
        else: 
            continue
    print(t)
    return t


if __name__ == '__main__':
    
    s = input()

    result = camelcase(s)

