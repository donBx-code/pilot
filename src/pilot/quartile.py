#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def calcMedian(x:list) -> float :
    
    print(x)
    sx = sorted(x)
    nx:int = len(sx)
    
    if nx % 2 ==1:
        md = sx[nx//2]
    else:
        md = ((sx[nx//2 - 1]) + (sx[nx//2]))/2
    
    return md

def quartiles(arr):
    # Write your code here
    items = sorted(arr)
    q = []

    #assumption : use 3 quartiles
    #if len(arr) % 2 == 1:
    q.append(int(calcMedian(items[:(n//2)])))
    q.append(int(calcMedian(items)))
    if len(arr) % 2 == 1:
        q.append(int(calcMedian(items[(n//2)+1:])))
    else:    
        q.append(int(calcMedian(items[(n//2):])))
        
    return q


  

if __name__ == '__main__':
    from io import StringIO


    # Store the original stdin
    original_stdin = sys.stdin

    #mydata = """9
    #3 7 8 5 12 14 21 13 18"""

    mydata ="""10
    3 7 8 5 12 14 21 15 18 14"""

    sys.stdin = StringIO(mydata)
    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    print(sorted(data))
    res = quartiles(data)

    print(res)

     # Restore the original stdin
    sys.stdin = original_stdin