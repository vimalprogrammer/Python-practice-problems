#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mincount=maxcount=0
    minscores=maxscores=scores[0]
    for i in range(1,len(scores)):
        if minscores<scores[i]:
            minscores=scores[i]
            mincount+=1
        if maxscores>scores[i]:
            maxscores=scores[i]
            maxcount+=1
    return mincount,maxcount
if __name__=='__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)