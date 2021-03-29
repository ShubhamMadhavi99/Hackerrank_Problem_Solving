#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0   #if total was divided between the 2
    t = 0       #if the item that Anna didn't eat is considered
    
    for i in bill:
        total = total + i

    y = bill[k]
    bill.remove(y)
    
    for j in bill:
        t = t + j
    
    if b == t / 2:
        print("Bon Appetit")
    else:
        print(int(total/2 - t/2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0   #if total was divided between the 2
    t = 0       #if the item that Anna didn't eat is considered
    
    for i in bill:
        total = total + i

    y = bill[k]
    bill.remove(y)
    
    for j in bill:
        t = t + j
    
    if b == t / 2:
        print("Bon Appetit")
    else:
        print(int(total/2 - t/2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
