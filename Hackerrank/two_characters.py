#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the alternate function below.
def alternate(s):
    for i in s:
        x = s.count(i)
        s.remove(max(x))
        

if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)
