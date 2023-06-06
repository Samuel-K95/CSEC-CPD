#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley=0
    curr=0
    for i in range((steps)):
        if curr==0:
            Track=path[i]
        if path[i]=='U':
            curr+=1
        elif path[i]=='D':
            curr-=1

        if curr==0 and Track=='U':
            continue
        elif curr==0 and Track=='D':
            valley+=1

        
    return (valley)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
