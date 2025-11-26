import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    wm  = []
    wi = 0

def weightedMean(X, W):
    # Write your code here
    wm  = 0.0
    wi = 0.0
    
    for i in range(len(X)):           
  
        wm += (X[i] * W[i])
        wi += W[i] 
                 
    #round to  1 decimal place
    return (round(wm/wi, 1))



if __name__ == '__main__':
    from io import StringIO


    # Store the original stdin
    original_stdin = sys.stdin


    myString = """5
    10 40 30 50 20
    1 2 3 4 5"""

    sys.stdin = StringIO(myString)

    
    #for s in ss:
     #   keyboard.type(ss)


    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    print(n)
    print(vals)
    print(weights)
    
    print(weightedMean(vals, weights))
   
    # Restore the original stdin
    sys.stdin = original_stdin