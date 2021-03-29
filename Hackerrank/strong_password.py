#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0    
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count,6-n)
   
    # numbers = "0123456789"
    # lower_case = "abcdefghijklmnopqrstuvwxyz"
    # upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # special_characters = "!@#$%^&*()-+"
    # if n < 6:
    #     return (6 - n)

    # else:
    #     if numbers in password:
    #         pass
    #     elif lower_case in password:
    #         pass
    #     elif upper_case in password:
    #         pass
    #     elif special_characters in password:
    #         pass
    #     else:
    #         return "1"
    
    # elif n >6:
    #     for i in password:
    #         if i in upper_case:
    #             continue
    #         else:
    #             return "1"

    #     for i in password:
    #         if i in lower_case:
    #             continue
    #         else:
    #             return "1"

    #     for i in password:
    #         if i in numbers:
    #             continue
    #         else:
    #             return "1"

    #     for i in password:
    #         if i in special_characters:
    #             continue
    #         else:
    #             return "1"
                

if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)

