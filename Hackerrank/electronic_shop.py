#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

x = n - 1
y = m - 1

total = keyboards[x] + drives[y]

if total > b:
    print("-1")
else:
    print(total)

    