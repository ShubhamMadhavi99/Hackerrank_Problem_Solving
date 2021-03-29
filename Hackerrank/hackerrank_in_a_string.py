

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    lst = []
    x = ['h','a','c','k','e','r','r','a','n','k']
    for i in s:
        if i in x:
            lst.append(i)
    print(lst)
    y = "".join(lst)
    print(y)
    
    if y.count('h') >= 1:
        if y.count('a') >= 2:
            if y.count('c') >= 1:
                if y.count('r') >= 2:
                    if y.count('k') >= 2:
                        if y.count('n') >= 1:
                            print("YES")
                        else:
                            print("NO")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

