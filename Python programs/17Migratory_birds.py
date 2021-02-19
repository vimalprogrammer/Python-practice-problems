#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    l=[0]*len(arr)
    for i in range(len(arr)):
        l[arr[i]]+=1#eg: l[4]+=1 count index value
    return l.index(max(l))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)