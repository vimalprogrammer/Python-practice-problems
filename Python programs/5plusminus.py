#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=neg=zero=0
    for i in range(n):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
            zero+=1
    a=(pos/n)
    b=(neg/n)
    c=(zero/n)
    print(round(a,6))
    print(round(b,6))
    print(round(c,6))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
