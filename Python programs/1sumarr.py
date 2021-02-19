#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    ar1=0
    for i in range(ar_count):
        ar1+=ar[i]
    return ar1
    #return sum(ar)

if __name__ == '__main__':
    fptr = open('C:/Users/vimalms/PycharmProjects/Elonmusk/c.txt', 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
