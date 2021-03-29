#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    
    a = ar.count(1)
    b = ar.count(2)
    c = ar.count(3)
    d = ar.count(4)
    e = ar.count(5)
    li=[a,b,c,d,e]
    result = print(1+li.index(max(li)))        
    return result  

if __name__ == '__main__':
    
    arr_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    

# #
# 6
# 1 4 4 4 5 3
# #
# 11
# 1 2 3 4 5 4 3 2 1 3 4