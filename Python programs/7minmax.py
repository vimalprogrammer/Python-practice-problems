#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s=0
    minimum=999999999999999
    maximum=0
    for i in range(len(arr)):
        s+=arr[i]
        minimum=min(minimum,arr[i])
        maximum=max(maximum,arr[i])
    print(s-maximum,s-minimum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
