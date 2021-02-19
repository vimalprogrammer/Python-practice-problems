#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftdiag=rightdiag=0
    for i in range(n):
        leftdiag+=arr[i][i]
        rightdiag+=arr[i][n-1-i]
    return abs(leftdiag-rightdiag)
    # Write your code here

if __name__ == '__main__':
    fptr = open('C:/Users/vimalms/PycharmProjects/Elonmusk/c.txt', 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
