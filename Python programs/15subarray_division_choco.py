#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    cnt=0
    total=sum(s[:m])

    if total==d:
        cnt+=1
    #sliding window
    for i in range(m,len(s)):
        total+=s[i]
        total-=s[i-m]
        if total==d:
            cnt+=1
    return cnt


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(result)