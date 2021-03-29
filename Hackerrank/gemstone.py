#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the gemstones function below.
def gemstones(arr):
    rocks = [set(input()) for _ in range(int(input()))]
    gems = set.intersection(*rocks)
    print(len(gems))


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

