#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    x = s.split(":")
    h = x[0]
    m = x[1]
    sec = x[2]
    s1 = sec[0]
    s2 = sec[1]
    
    if sec[2] == "A":
        if h == "12":
            h = "00"
            result = (h+":"+m+":"+s1+s2)
            print(result)
            return result
        else:
            result = (h+":"+m+":"+s1+s2)
            print(result)
            return result
    if sec[2] == "P":
        if h == "12":
            result =(str(h)+":"+m+":"+s1+s2)
            print(result)
            return result
        else:
            h = int(h) + 12
            result =(str(h)+":"+m+":"+s1+s2)
            print(result)
            return result
    
if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)

    
