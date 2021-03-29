#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxHeight=0
    for i in range(len(word)):
	    if(h[ord(word[i])-97] > maxHeight):
		    maxHeight=h[ord(word[i])-97]
    return (len(word)*1*maxHeight)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

