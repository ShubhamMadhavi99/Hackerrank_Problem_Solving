#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the superReducedString function below.

def superReducedString(s):
    current = 0
    while current < len(s) - 1:
        if s[current] == s[current+1]:
            s = s[:current] + s[current+2:]
            current = 0
        else:
            current += 1
    if s:
        return s
    else:
        return 'Empty String'

if __name__ == '__main__':

    s = input()

    result = superReducedString(s)
    
    print(result)
