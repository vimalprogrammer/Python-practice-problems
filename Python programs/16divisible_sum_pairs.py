#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):#for i<j
            if (ar[i]+ar[j])%k==0:
                cnt+=1
    return cnt



if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)